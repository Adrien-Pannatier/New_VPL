"""
Author: Adrien Pannatier
Date of Creation: 16.05.2024
Description: you can use this script to delete a block from the block list using the block name. 
             command: python delete_block.py [block_name]
"""

import json
import argparse

def delete_from_block_list(name):
    with open('svg/block-list.json', 'r') as file:
        data = json.load(file)
        
    for key in data.keys():
        for item in data[key]:
            if item == name:
                data[key].remove(item)
                print(f"Deleted block {name} from block list")
                with open('svg/block-list.json', 'w') as file:
                    json.dump(data, file, indent=4)
                return

    print(f"⚠️ Block {name} not found in block list")

def delete_from_languages(name):
    languages = ["de", "en", "fr", "it"]
    for lang in languages:
        path = f'svg/help-blocks-{lang}.json'
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        
        for element in data['help'][lang]['blocks']:
            if element == name:
                del data['help'][lang]['blocks'][element]
                print(f"Deleted block {name} from {lang} help file")
                with open(path, 'w') as file:
                    json.dump(data, file, indent=4)
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="The name of the block to delete")
    args = parser.parse_args()

    delete_from_languages(args.name)

    # # ask for confirmation
    # confirmation = input(f"Are you sure you want to delete block {args.name} from block list? (y/n) ")

    # if confirmation == 'y':
    #     delete_from_block_list(args.name)
    # else:
    #     print("Block deletion cancelled")