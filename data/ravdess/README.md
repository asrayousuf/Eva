1. Download RAVDESS data online manually or using `download.sh`

2. Unzip all .zip files manually or using `unzip.sh`.

3. There should be a folder each for each actor with videos inside. Take out all videos from the subdirectories.

3. Create subdirectories for each emotion in the following format: `0?.emotion`

4. Run `classify_data.py`. All videos will be put in their respective emotion folders.

5. Run `extract_frames.py` in each folder. This will retrieve all the images from the videos every second on the folder.
