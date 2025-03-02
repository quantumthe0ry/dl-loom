# dl-loom

A small Python 3 script to download Loom videos by session ID.

# Description
`dl-loom.py` takes a Loom video session ID and makes a POST request to Loom’s API to retrieve the transcoded URL. It then downloads the video file to your local machine, complete with a progress indicator.

## Requirements
-   [Python 3](https://www.python.org/)
-   [Requests library](https://pypi.org/project/requests/) (install via `pip install requests`)

## Installation

-   **Clone** (or download) this repository:  
    `git clone https://github.com/quantumthe0ry/dl-loom.git` 
    
-   **Navigate** into the repository folder:    
    `cd dl-loom` 
-   **Install** dependencies:
    `pip install requests`
## Usage
-   **Run** the script:
    `python3 dl-loom.py -id YOUR_VIDEO_ID -o OUTPUT_FILE.mp4`

## What is your video ID?

The shared Loom video will have a URL similar to this:
`https://www.loom.com/share/a30d0e744d2889e89f458c50061e33ed?sid=`
In this example, the video ID would be **a30d0e744d2889e89f458c50061e33ed**.

Therefore, to run the script, simply do: 
`python3 dl-loom.py -id a30d0e744d2889e89f458c50061e33ed -o file.mp4`
