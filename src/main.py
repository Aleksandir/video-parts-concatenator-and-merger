# Import the os and moviepy modules
import os
import re

from moviepy.editor import VideoFileClip, concatenate_videoclips


def get_unique_filename(base_path, filename):
    counter = 1
    name, extension = os.path.splitext(filename)
    new_filename = filename

    while os.path.exists(os.path.join(base_path, new_filename)):
        new_filename = f"{name}_{counter}{extension}"
        counter += 1

    return new_filename


def get_video_files(dir_path):
    return [
        f
        for f in os.listdir(dir_path)
        if os.path.isfile(os.path.join(dir_path, f)) and f.endswith(".mp4")
    ]


def sort_video_files(video_files):
    return sorted(
        video_files,
        key=lambda x: int(re.search(r"(\d+)\.mp4$", x).group(1))
        if re.search(r"(\d+)\.mp4$", x) is not None
        else 0,
    )


def create_video_clips(video_files, dir_path):
    return [VideoFileClip(os.path.join(dir_path, file)) for file in video_files]


def main():
    # Define the directory path where the videos are stored
    dir_path = input("Enter the directory path: ")
    while True:
        for file in os.listdir(dir_path):
            if file.endswith(".mp4"):
                print(file)

        proceed = input("\nIs this the correct directory? (y/n): ").lower()
        if proceed == "y":
            break
        else:
            dir_path = input("Enter the directory path: ")

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
            base_path = "videos/concatinated_vidoes"
            filename = "final.mp4"
            unique_filename = get_unique_filename(base_path, filename)
            final_clip.write_videofile(os.path.join(base_path, unique_filename))
        else:
            print("No video clips found.")


main()
