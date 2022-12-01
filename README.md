# ExDark2Yolo
### Convert ExDark annotated data format to YOLO format data
  - The ExDark data directory structure is as follows:
    ```text
      ExDark_dataset
        ├── Annotations
        │    └── Bicycle
        │         ├── image1.jpg.txt
        │         └── image2.jpg.txt
        └── Images
             └── Bicycle
                  ├── image1.jpg
                  └── image2.jpg
    ```
  - Convert
    ```shell
    python exDark2Yolo.py --annotations-dir dataset/Annotations/ \
                          --images-dir dataset/images/ \
                          --output-dir output/
    ```
    - `--annotations-dir`: ExDark annotations Directory, end with '/'.
    - `--images-dir`: ExDark images Directory, end with '/'.
    - `--output-dir`: (optional) Output Directory, end with '/'.

  - Converted directory structure (output directory):
    ```text
         output
           └── Bicycle
                 ├── image1.jpg.txt
                 └── image2.jpg.txt
    ```