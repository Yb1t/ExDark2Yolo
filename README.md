# ExDark2Yolo
### Convert ExDark annotated data format to YOLO format data
  - The ExDark data directory structure is as follows:
    ```text
      ExDark_dataset
        ├── annotations
        │   ├── Bicycle
        │   ├── Boat
        │   ...
        └── images
            ├── Bicycle
            ├── Boat
            ...
    ```
    
  - Convert
    ```shell
    python exDark2Yolo.py --annotations-dir dataset/annotations \
                          --images-dir dataset/images \
                          --ratio 8:1:1 \
                          --output-dir output
    ```
    - `--annotations-dir`: ExDark annotations directory.
    - `--images-dir`: ExDark images directory.
    - `--ratio`: (optional) Ratio between train/test/val, default 8:1:1.
    - `--output-dir`: (optional) Images and annotations output directory.

  - Converted directory structure (output directory):
    ```text
      output
        ├── images
        │   ├── test
        │   ├── train
        │   └── val
        └── labels
            ├── test
            ├── train
            └── val
    ```