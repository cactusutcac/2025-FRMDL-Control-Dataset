import os
import cv2
import random
from glob import glob

INPUT_DIR = "IXMAS_32" # Folder with original 32-frame .avi videos
OUTPUT_DIR = "IXMAS_shuffled"
NUM_FRAMES = 32
CHUNK_SIZE = 8
SEED = 0

os.makedirs(OUTPUT_DIR, exist_ok=True)
random.seed(SEED)

# Extract exactly 32 frames from a video 
def load_video_frames(video_path, num_frames=NUM_FRAMES):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while len(frames) < num_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames if len(frames) == num_frames else None

# Shuffle 4 equal-length chunks 
def shuffle_chunks(frames, chunk_size=8):
    chunks = [frames[i:i + chunk_size] for i in range(0, len(frames), chunk_size)]
    original_order = list(range(len(chunks)))
    shuffled_order = original_order[:]

    # Keep shuffling until it's different from the original 
    while True:
        random.shuffle(shuffled_order)
        if shuffled_order != original_order:
            break

    # Reorder chunks
    shuffled_chunks = [chunks[i] for i in shuffled_order]
    return [frame for chunk in shuffled_chunks for frame in chunk]

video_files = glob(os.path.join(INPUT_DIR, "*.avi"))

for vid_path in video_files:
    filename = os.path.basename(vid_path)

    frames = load_video_frames(vid_path)
    if frames is None:
        print(f"Skipped {filename} (not exactly {NUM_FRAMES} frames). ")
        continue

    shuffled = shuffle_chunks(frames)

    # Save shuffled video
    height, width, _ = shuffled[0].shape
    out_path = os.path.join(OUTPUT_DIR, filename)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(out_path, fourcc, 25.0, (width, height))
    for frame in shuffled:
        out.write(frame)
    out.release()
