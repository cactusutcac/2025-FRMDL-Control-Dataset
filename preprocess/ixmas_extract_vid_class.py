import os

video_dir = "IXMAS"

# Set of action class names to keep
allowed_classes = {
    "check-watch", "point", "kick",
    "sit-down", "get-up", "walk"
}

for filename in os.listdir(video_dir):

    # Check if the filename contains one of the allowed classes
    if not any(action in filename for action in allowed_classes):
        # Delete the file if it's not an allowed class
        file_path = os.path.join(video_dir, filename)
        os.remove(file_path)
