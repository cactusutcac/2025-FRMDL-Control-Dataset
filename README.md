# A Controlled Dataset to Evaluate Temporal Sensitivity in BDQ Encoding 
## Project Overview 
This repository provides the code and data pipeline for constructing a control dataset designed to evaluate the **temporal sensitivity** of the BDQ encoder introduced in the paper _Privacy-Preserving Action Recognition via Motion Difference Quantization_ [1]. 

The goal is to test whether BDQ's performance in action recognition and identity suppression truly relies on inter-frame motion cues. Based on a subset of the IXMAS dataset, we construct two matched conditions for each video clip: 
- Original sequences: 32 consecutive frames with intact temporal order 
- Shuffled sequences: the same frames divided into 4 chunks of 8 and randomly reordered to disrupt global temporal flow 

## Directory Structure 
### Datasets & Metadata 
- Raw datasets available from [IXMAS Actions – New Views and Occlusions - CVLAB - EPFL](https://www.epfl.ch/labs/cvlab/data/data-ixmas10/) 
- `datasets/ixmas_clips_6.json`: structured metadata such as action and subject ID for selected clips 

### Preprocessing Scripts 
- `preprocess/IXMAS_720`: 720 manually selected representative frames (10 subject $\times$ 12 classes $\times$ 2 viewpoints $\times$ 3 takes)
- `preprocess/ixmas_extract_frame.py`: extracts and saves a representative frame from each IXMAS video 
- `preprocess/ixmas_extract_vid.py`: copies videos matching selected frame names (e.g., from `IXMAS_720/`) 
- `preprocess/ixmas_extract_vid_class.py`: filters and saves videos of the six selected action classes 
- `preprocess/ixmas_parser.py`: parses video filenames into structured metadata 

## Control Dataset Construction 
1. Download and organize raw data
   Download the `original IXMAS ROIs` and place it under the `preprocess/IXMAS_raw/`. 
2. Install dependencies: 
```bash
pip install -r requirements.txt
```
1. Preprocess original dataset: 
```bash
# Optional: extract one representative frame from each video
# python preprocess/ixmas_extract_frame.py

python preprocess/ixmas_extract_vid.py # Extract all videos from chosen frames 
python preprocess/ixmas_extract_vid_6.py # Keep only the 6 selected actions
python preprocess/ixmas_parser.py # Generate structured metadata 
```
1. Generate the control dataset:  
```bash
python trim_vid.py # Cut videos to exactly 32 consecutive frames 
python shuffle_chunks.py # Shuffle each video 
```

## References 
[1] S. Kumawat and H. Nagahara, “Privacy-Preserving Action Recognition via Motion Difference Quantization,” Aug. 2022.

[2] D. Weinland, R. Ronfard, and E. Boyer, “Free viewpoint action recognition using motion history volumes,” Computer Vision and Image Understanding, vol. 104, pp. 249–257, Nov. 2006. 
