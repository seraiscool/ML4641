import os
import argparse
import pandas as pd
from get_dex_name_csv import extract_dict_from_csv
import re 
import pprint

def rename_images_by_dex(label_csv, img_dir):
    data = pd.read_csv(label_csv)
    imgs = os.listdir(img_dir)
    data = extract_dict_from_csv(file=label_csv)
    # import pdb; pdb.set_trace()
    missing = []
    for img in imgs:
        val = re.findall(r'\d+', img)[0]
        if val not in data:
            missing.append(val)
        new_img = img.replace(val, data[val])
        os.rename(os.path.join(img_dir, img), os.path.join(img_dir,new_img))
    print("Missing values: ")
    pprint.pprint(missing)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--label_csv', '-l', type=str, required=True)
    parser.add_argument('--img_dir', '-i', type=str, required=True)
    args = parser.parse_args()
    rename_images_by_dex(args.label_csv, args.img_dir)
    