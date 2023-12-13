import os
import re

from moviepy.editor import VideoFileClip, concatenate_videoclips


def get_unique_filename(base_path, filename):
    """
    Generate a unique filename by appending a counter to the base filename if it already exists in the specified directory.

    Args:
        base_path (str): The base path of the directory where the file is located.
        filename (str): The original filename.

    Returns:
        str: The unique filename.

    """
    counter = 1
    name, extension = os.path.splitext(filename)
    new_filename = filename

    while os.path.exists(os.path.join(base_path, new_filename)):
        new_filename = f"{name}_{counter}{extension}"
        counter += 1

    return new_filename


def get_video_files(dir_path):
    """
    Get a list of video files (.mp4) in the specified directory.

    Args:
        dir_path (str): The path to the directory.

    Returns:
        list: A list of video file names.

    """
    return [
        f
        for f in os.listdir(dir_path)
        if os.path.isfile(os.path.join(dir_path, f)) and f.endswith(".mp4")
    ]


def sort_video_files(video_files):
    """
    Sorts a list of video file names based on the numeric value in the file name.

    Args:
        video_files (list): A list of video file names.

    Returns:
        list: The sorted list of video file names.
    """
    return sorted(
        video_files,
        key=lambda x: int(re.search(r"(\d+)\.mp4$", x).group(1))
        if re.search(r"(\d+)\.mp4$", x) is not None
        else 0,
    )


def create_video_clips(video_files, dir_path):
    """
    Create video clips from a list of video files.

    Args:
        video_files (list): List of video file names.
        dir_path (str): Directory path where the video files are located.

    Returns:
        list: List of video clips created from the video files.
    """
    return [VideoFileClip(os.path.join(dir_path, file)) for file in video_files]


def main():
    dir_path = input("Enter the directory path: ")
    while True:
        # List all the video files in the directory
        for file in os.listdir(dir_path):
            if file.endswith(".mp4"):
                print(file)

        proceed = input("\nIs this the correct directory? (y/n): ").lower()
        if proceed == "y":
            break
        else:
            dir_path = input("Enter the directory path: ")

    # Get a list of video files in the directory and sort them
    video_files = get_video_files(dir_path)
    video_files = sort_video_files(video_files)

    print("**File order**\n")
    # Print the list of video files and their index for user verify order
    for i, video in enumerate(video_files):
        print(i, video)

    proceed = input("\nProceed? (y/n): ")
    if proceed == "y":
        # Create a list of VideoFileClip objects for each video file
        clips = create_video_clips(video_files, dir_path)

        if clips:
            final_clip = concatenate_videoclips(clips)

            # Write the output video file
            filename = "final.mp4"
            unique_filename = get_unique_filename(dir_path, filename)
            final_clip.write_videofile(os.path.join(dir_path, unique_filename))
        else:
            print("No video clips found.")


main()
