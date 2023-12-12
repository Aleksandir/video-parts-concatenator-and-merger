# Video Processing Script

This Python script reads video files from a specified directory, sorts them based on the part numbers in their names, and concatenates them into a single video file.

## Requirements

The script requires Python 3 and the following Python packages:

- moviepy

You can install the required packages with the following command:

```sh
pip install -r requirements.txt
```

## Running the Script

You can run the script with the following command:

```sh
python src/main.py
```

The script reads the video files from the specified directory, sorts them, and concatenates them into a single video file. The output video file is saved as `final.mp4` in the current directory.

## Video File Names

The video files should have part numbers in their names in the format "FILENAME Pt 6.mp4", where "6" is the part number. The script sorts the video files based on these part numbers. The part number can be located anywhere in the file name, but it must be the last number before the `.mp4` extension.
