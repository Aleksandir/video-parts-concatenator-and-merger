# Video Processing Script

This Python script reads video files from a specified directory, sorts them based on the part numbers in their names, and concatenates them into a single video file.

## Running the Script

To run this project, follow these steps:

1. Make sure you have Python 3 on your computer. If not, you can get it from this website: [python.org](https://www.python.org/downloads/).

2. Open the program where you type commands (like Terminal on Mac, or Command Prompt on Windows).

3. Go to the place on your computer where you want to put the project.

4. Copy the project to your computer by typing this command:

   \```sh
   git clone https://github.com/your-username/video-processing-script.git
   \```

   Replace `your-username` with your own GitHub username.

5. Go into the project folder by typing:

   \```sh
   cd video-processing-script
   \```

Note: If you don't have Git (the tool that lets you copy the project), you can get it from this website: [git-scm.com](https://git-scm.com/downloads).

6. Install the things Python needs to run the project by typing:

   \```sh
   pip install -r requirements.txt
   \```

   This will get everything ready for running the script.

7. Start the script by typing:

   \```sh
   python src/main.py
   \```

   The script will start working on the video files in the chosen place.

8. Wait for the script to finish. It will put all the videos together into one video file named `final.mp4`.

9. When the script is done, the final video will be in the same place as the original videos, and it will be called `final.mp4`.

Note: Make sure that the video files in the specified directory have part numbers in their names in the format "FILENAME Pt 6.mp4", where "6" is the part number. The script will sort the video files based on these part numbers. The part number can be located anywhere in the file name, but it must be the last number before the `.mp4` extension.
