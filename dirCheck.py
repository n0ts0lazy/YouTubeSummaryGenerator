# Import os module
import os

# Function to create 'video cache' and 'result' folders if they don't exist
def createFolders():
    try:
        # Check if 'video cache' folder exists, and create it if not
        video_cache_folder = 'Video cache'
        if not os.path.exists(video_cache_folder):
            os.makedirs(video_cache_folder)

        # Check if 'result' folder exists, and create it if not
        result_folder = 'Result'
        if not os.path.exists(result_folder):
            os.makedirs(result_folder)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Call the createFolders function when this script is run
    createFolders()
