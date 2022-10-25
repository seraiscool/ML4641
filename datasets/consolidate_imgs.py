import os
import argparse
import subprocess

def copy_imgs(src_dirs, dest_dir, override=False):
    '''
    Arguments:
        src_dirs: a list of directories from which images are being copied
        dest_dir: the directory where all images will be saved
        override: how to handle if an image already exists in the dest_dir;
                  by default, it will not override the existing image and 
                  saves another image with a modified filename. 
    '''
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    for src_dir in src_dirs:
        # import pdb; pdb.set_trace()
        imgs = os.listdir(src_dir)
        imgs = list(filter((lambda x: '.png' in x or '.jpg' in x), imgs))
        for img in imgs:
            img_path = os.path.join(dest_dir, img)
            if not os.path.exists(img_path) or override:
                cp_cmd = 'cp ' + os.path.join(src_dir, img) + " " + img_path
                subprocess.call(cp_cmd, shell=True)
                continue
            img_wo_ext = os.path.splitext(img)[0]
            new_img = img_wo_ext + '1.png'
            img_path = os.path.join(dest_dir,new_img)
            cp_cmd = 'cp ' + os.path.join(src_dir, img) + " " + img_path 
            subprocess.call(cp_cmd, shell=True)

if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument('--dest_dir', '-d', type=str, required=True)
    parser.add_argument('--src_dirs', '-i', type=str, nargs='+' , required=True)
    parser.add_argument('--override', '-o', type=bool, default=False)
    parser_args = parser.parse_args()
    src_dirs = parser_args.src_dirs
    dest_dir = parser_args.dest_dir
    override = parser_args.override
    copy_imgs(src_dirs, dest_dir, override)