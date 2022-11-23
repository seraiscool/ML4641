import os
import argparse
import subprocess
import pandas as pd

def extract_dict_from_csv(file):
    '''
    Takes the pokemon-type csv and extracts a dict mapping pokedex number
    to pokemon name. 
    '''
    data = pd.read_csv(file)
    names = data["Name"]
    type_1 = data["Type1"]
    type_2 = data["Type2"]
    pokeDict = {}
    for name, t1, t2 in zip(names, type_1, type_2):
        if (name not in pokeDict):
            if (t2 != 'Flying'):
                pokeDict[name] = [t1, t2]
            else:
                pokeDict[name] = [t2, t1]
    return pokeDict

def save_comp_labels(pokeDict, img_dir, save_dir):
    '''
    Creates the new composite image csv assosciating image name to types; flipped flying 
    types due to data imbalance
    '''
    names=[]
    type1=[]
    type2=[]
    # import pdb; pdb.set_trace()
    for img in os.listdir(img_dir):
        for name in pokeDict:
            if (name in img):
                names.append(img)
                type1.append(pokeDict[name][0])
                type2.append(pokeDict[name][1])
    data = pd.DataFrame({"Name": names, "type1": type1, "type2":type2})
    data.to_csv(os.path.join(save_dir, "composite_labels.csv"), index=False)


if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_dir', '-i', type=str, required=True)
    parser.add_argument('--csv_path', '-c', type=str, default=True)
    parser.add_argument('--save_dir', '-s', type=str, default=os.getcwd())
    parser_args = parser.parse_args()
    save_dir = parser_args.save_dir
    csv_path = parser_args.csv_path
    img_dir = parser_args.img_dir
    pokeDict = extract_dict_from_csv(csv_path)
    save_comp_labels(pokeDict, img_dir, save_dir)
