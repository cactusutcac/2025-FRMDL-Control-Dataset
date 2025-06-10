import os
import cv2
from glob import glob

INPUT_DIR = "IXMAS"
OUTPUT_DIR = "IXMAS_32"
NUM_FRAMES = 32

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Extract and save first 32 frames
def trim_video(input_path, output_path, num_frames=NUM_FRAMES):
    cap = cv2.VideoCapture(input_path)
    frames = []
    while len(frames) < num_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()

    if len(frames) < num_frames:
        print(f"Skipped {os.path.basename(input_path)} (only {len(frames)} frames found).")
        return

    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 25.0, (width, height))
    for frame in frames:
        out.write(frame)
    out.release()

video_paths = glob(os.path.join(INPUT_DIR, "*.avi"))
for path in video_paths:
    filename = os.path.basename(path)
    output_path = os.path.join(OUTPUT_DIR, filename)
    trim_video(path, output_path)

