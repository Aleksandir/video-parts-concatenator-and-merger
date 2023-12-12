# Video Processing Script

This Python script reads video files from a specified directory, sorts them based on the part numbers in their names, and concatenates them into a single video file.

## Running the Script

To run this project, follow these steps:

1. Ensure that you have Python 3 installed on your computer. You can download it from the official Python website: [python.org](https://www.python.org/downloads/).

2. Open a command prompt or terminal window.

3. Navigate to the directory where you have downloaded or cloned this project.

   1. this can be done by running the following command:

      ```sh
      cd path/to/directory
      ```

      Replace `path/to/directory` with the actual path to the directory where you have downloaded or cloned this project.

4. Install the required Python packages by running the following command:

   ```sh
   pip install -r requirements.txt
   ```

   This command will install the necessary packages for running the script.

5. Once the packages are installed, run the script with the following command:

   ```sh
   python src/main.py
   ```

   The script will start processing the video files in the specified directory.

6. Wait for the script to finish processing the videos. It will concatenate them into a single video file named `final.mp4`.

7. Once the script has finished running, you can find the final video file in the same directory where you ran the script.

Note: Make sure that the video files in the specified directory have part numbers in their names in the format "FILENAME Pt 6.mp4", where "6" is the part number. The script will sort the video files based on these part numbers. The part number can be located anywhere in the file name, but it must be the last number before the `.mp4` extension.
