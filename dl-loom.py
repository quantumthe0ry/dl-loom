#!/usr/bin/env python3

import argparse
import requests
import sys
import math

def download_file(url, output_filename):
    """Download file from 'url' into 'output_filename' with progress indicator."""
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_length = r.headers.get('content-length')
        
        # If we know the total size, we can show a progress indicator
        if total_length is not None:
            total_length = int(total_length)
        
        downloaded = 0
        chunk_size = 8192
        
        print(f"📥 Downloading and saving as: {output_filename}")
        with open(output_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_length is not None:
                        percent_done = math.floor((downloaded / total_length) * 100)
                        # Print on one line, flush, then overwrite
                        sys.stdout.write(f"\r📥 Downloading ... {percent_done}%")
                        sys.stdout.flush()
        
        # If we didn't know the total length, just say 100% at the end
        if total_length is None:
            sys.stdout.write("\r📥 Downloading ... 100%\n")
        print(f"\n✅ Download complete: {output_filename}\n")

def main():
    parser = argparse.ArgumentParser(description='Download Loom video by ID.')
    parser.add_argument("-id", "--id", required=True, help="The Loom session ID")
    parser.add_argument("-o", "--output", required=True, help="Output filename (e.g. file.mp4)")
    args = parser.parse_args()
    
    # Construct the endpoint
    endpoint = f"https://www.loom.com/api/campaigns/sessions/{args.id}/transcoded-url"
    
    print(f"🎬 Fetching video ID: {args.id} ...")
    
    # Make POST request
    response = requests.post(endpoint)
    response.raise_for_status()
    
    data = response.json()
    
    # The JSON should contain a key named "url"
    video_url = data.get("url")
    
    if not video_url:
        print("❌ Error: Could not find 'url' in response. Exiting.")
        sys.exit(1)
    
    print(f"🔗 Video URL: {video_url}")
    
    # Download the file
    download_file(video_url, args.output)

if __name__ == "__main__":
    main()
