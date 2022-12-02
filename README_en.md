# ExDark2Yolo
### Convert ExDark annotated format data to YOLO format data
[简体中文](./README.md) | English
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
    
  - Convert:
    ```shell
    python exDark2Yolo.py --annotations-dir dataset/annotations \
                          --images-dir dataset/images \
                          --ratio 8:1:1 \
                          --output-dir output
    ```
    - `--annotations-dir`: ExDark annotations directory.
    - `--images-dir`: ExDark images directory.
    - `--ratio`: (optional) Ratio between train/test/val, default 8:1:1.
    - `--output-dir`: (optional) Images and converted YOLO annotations output directory.

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