import os
from PIL import Image
import argparse

labels = ['Bicycle', 'Boat', 'Bottle', 'Bus', 'Car', 'Cat', 'Chair', 'Cup', 'Dog', 'Motorbike', 'People', 'Table']


def ExDark2Yolo(txts_path, photos_path, output_path):
    for label in labels:
        print('Processing %s...' % label)
        filenames = os.listdir(txts_path + label)
        os.makedirs(output_path + label + '/train')
        os.makedirs(output_path + label + '/val')
        os.makedirs(output_path + label + '/test')
        cur_idx = 0
        files_num = len(filenames)

        for filename in filenames:
            cur_idx += 1
            if cur_idx < files_num*0.8:
                path = output_path + label + '/train/' + filename
            elif cur_idx < files_num*0.9:
                path = output_path + label + '/val/' + filename
            else:
                path = output_path + label + '/test/' + filename
            yolo_output_file = open(path, 'a')

            txt = open(txts_path + label + '/' + filename, 'r')

            try:
                img = Image.open(photos_path + label + '/' + '.'.join(filename.split('.')[:-1]))
            except FileNotFoundError:
                name_split = filename.split('.')
                img = Image.open(photos_path + label + '/' + '.'.join(name_split[:-2]) + '.' + name_split[-2].upper())

            width, height = img.size

            txt.readline()  # ignore first line
            line = txt.readline()

            while line != '':
                datas = line.strip().split()

                class_idx = labels.index(datas[0])
                x = int(datas[1]) / width
                y = int(datas[2]) / height
                w = int(datas[3]) / width
                h = int(datas[4]) / height

                yolo_output_file.write(' '.join([str(class_idx),
                                                 format(x, '.5f'),
                                                 format(y, '.5f'),
                                                 format(w, '.5f'),
                                                 format(h, '.5f'),
                                                 ])+'\n')
                line = txt.readline()

            yolo_output_file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--annotations-dir', type=str, required=True, help="ExDark annotations Directory, end with '/'")
    parser.add_argument('--images-dir', type=str, required=True, help="ExDark images Directory, end with '/'")
    parser.add_argument('--output-dir', type=str, default="output/")
    args = parser.parse_args()
    ExDark2Yolo(args.annotations_dir, args.images_dir, args.output_dir)

