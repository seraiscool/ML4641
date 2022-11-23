import os
import argparse
import pandas as pd

def extract_dict_from_csv(file, save=False):
    '''
    Takes the pokedex csv and extracts a dict mapping pokedex number
    to pokemon name. 
    '''
    data = pd.read_csv(file)
    dexNums = data['#']
    dexNames = data['Name']

    # Remove Mega/additional forms to align data size with original dataset. 
    pokeDict = {}
    for num, name in zip(dexNums, dexNames):
        if (str(num) not in pokeDict):
            pokeDict[str(num)] = name.lower().split('-')[0]
        else: 
            continue
    if save:
        csv_path = "dex-name.csv"
        if os.path.exists(csv_path):
            override = input("dex-name.csv already exists. Do you wish to override? (Y/N) ").lower()
            print(override)
            while override != 'n' and override != 'y':
                override = input("dex-name.csv already exists. Do you wish to override? (Y/N) ").lower()
            if override == 'n':
                return pokeDict
        nums = pokeDict.keys()
        names = pokeDict.values()
        data = {'#': nums, 'Name': names}
        pokeDF = pd.DataFrame(data)
        pokeDF.to_csv(csv_path, index=False)
    return pokeDict

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--label_csv', '-l', type=str, required=True)
    parser.add_argument('--save_labels', '-sl', type=bool, default= False, required=False)
    parser_args = parser.parse_args()
    extract_dict_from_csv(parser_args.label_csv, parser_args.save_labels)