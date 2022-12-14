# ExDark2Yolo
### 将ExDark标注格式的数据转换成YOLO格式的数据
简体中文 | [English](./README_en.md)
  - ExDark的数据目录结构如下:
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
    
  - 转换:
    ```shell
    python exDark2Yolo.py --annotations-dir dataset/annotations \
                          --images-dir dataset/images \
                          --ratio 8:1:1 \
                          --version 5 \
                          --output-dir output
    ```
    - `--annotations-dir`：ExDark的标注目录。
    - `--images-dir`：ExDark的图像目录。
    - `--ratio`：（可选）train/test/val之间的比例，默认为8:1:1。
    - `--version`：（可选）YOLO版本（3或5），默认为5。
    - `--output-dir`: （可选）图像和转换后的yolo标注的输出目录。

  - 转换后的目录结构（输出目录）:
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
    
  - 输出下载：
    - YOLOv5： [百度网盘](https://pan.baidu.com/s/1o_zBJ9ZTbDGNZz3TUjUuYQ) | 提取码：zf76 （由 [@Mr-ind1fferent](https://github.com/Mr-ind1fferent) 提供）