from PIL import Image 
import argparse
import os

def convert_imgs(src_dirs, file_format, replace=True):
    '''
    Arguments:
        src_dirs: a list of image directories where the conversion is to take place
        file_format: the desired file format extension; expects png or jpg
        replace: whether to replace the existing image file of the same name
                 or simply create the new file with the desired extension
    '''
    file_format = '.' + file_format.strip('.')
    # import pdb; pdb.set_trace()
    for src_dir in src_dirs:
        imgs = os.listdir(src_dir)
        imgs = list(filter((lambda x: file_format not in x), imgs))
        for img in imgs:
            new_img = Image.open(os.path.join(src_dir, img))
            img_name = os.path.splitext(img)[0] + file_format
            new_img.save(os.path.join(src_dir, img_name))
            if replace:
                os.remove(os.path.join(src_dir, img))




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--src_dirs', '-s', type=str, nargs='+', required=True)
    parser.add_argument('--file_format', '-f', type=str, choices=['png', 'jpg', '.jpg', '.png'], required=True)
    parser.add_argument('--replace', '-r', type=bool, default=True)
    parser_args = parser.parse_args()
    file_format = parser_args.file_format
    src_dirs = parser_args.src_dirs
    replace = parser_args.replace
    convert_imgs(src_dirs, file_format, replace)
