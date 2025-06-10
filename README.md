# A Controlled Dataset to Evaluate Temporal Sensitivity in BDQ Encoding 
_Privacy-Preserving Action Recognition via Motion Difference Quantization_ ?

## Project Overview 
? 

## Directory Structure 
### Datasets & Metadata 
- Raw datasets available from at [IXMAS Actions – New Views and Occlusions - CVLAB - EPFL](https://www.epfl.ch/labs/cvlab/data/data-ixmas10/) 
- `datasets/ixmas_clips_6.json`: structured clip metadata generated from parsers 

### Preprocessing Scripts 
- `preprocess/IXMAS_720`: 720 manually selected representative frames (10 subject, 12 classes, 2 viewpoints, 3 performance of each action)
- `preprocess/ixmas_extract_frame.py`: extracts and saves a representative frame from each IXMAS video 
- `preprocess/ixmas_extract_vid.py`: locates and copies videos matching selected frame names (e.g., for `IXMAS_720/`) 
- `preprocess/ixmas_extract_vid_class.py`: filters and saves videos belonging to six selected actions 
- `preprocess/ixmas_parser.py`: generates clip metadata from IXMAS video filenames 

## Control Dataset Construction 
1. Downoload the raw dataset (`original IXMAS ROIs`) from and save it under the folder `preprocess/IXMAS_raw`. 
2. Install requirements: 
```bash
pip install -r requirements.txt
```
3. Preprocess the original dataset: 
```bash
python preprocess/ixmas_extract_vid.py
python preprocess/ixmas_extract_vid_6.py
python preprocess/ixmas_parser.py
```
4. Generate the control dateset:  
```bash
?
```

## References 
[1] S. Kumawat and H. Nagahara, “Privacy-Preserving Action Recognition via Motion Difference Quantization,” Aug. 2022.

[2] D. Weinland, R. Ronfard, and E. Boyer, “Free viewpoint action recognition using motion history volumes,” Computer Vision and Image Understanding, vol. 104, pp. 249–257, Nov. 2006. 
