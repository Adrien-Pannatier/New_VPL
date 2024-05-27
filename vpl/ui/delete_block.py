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

def delete_from_help_languages(name):
    languages = ["de", "en", "fr", "it"]
    for lang in languages:
        delete = False
        path = f'svg/help-blocks-{lang}.json'
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        
        for element in data['help'][lang]['blocks']:
            if element == name:
                del data['help'][lang]['blocks'][element]
                print(f"Deleted block {name} from {lang} help file")
                delete = True
                with open(path, 'w') as file:
                    json.dump(data, file, indent=4)
                break
        
        if not delete:
            print(f"⚠️ Block {name} not found in {lang} help file")

def delete_from_block_description_language(name):
    languages = ["de", "en", "fr", "it"]
    for lang in languages:
        delete = False
        path = f'svg/block-{lang}.json'
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)

        for element in data['i18n'][lang]:
            if element == name:
                del data['i18n'][lang][element]
                print(f"Deleted block {name} from {lang} description file")
                delete = True
                with open(path, 'w') as file:
                    json.dump(data, file, indent=4)
                break
                
        if not delete:
            print(f"⚠️ Block {name} not found in {lang} description file")

def delete_from_code_files(name):
    code_languages = ["aseba", "js", "python", "l2"]
    # code_languages = ["aseba"]

    for lang in code_languages:
        delete = False
        path = f'svg/{lang}.json'
        with open(path, 'r') as file:
            data = json.load(file)

        for i,element in enumerate(data['blocks']):
            if element['name'] == name:
                try: 
                    # print(element[lang])
                    del data['blocks'][i]
                    print(f"Deleted block {name} from {lang} code file")
                    delete = True
                    with open(path, 'w') as file:
                        json.dump(data, file, indent=4)
                    break
                except:
                    print(f"ERROR: No translation found in {lang} code file")

        if not delete:
            print(f"⚠️ Block {name} not found in {lang} code file")

def delete_from_ui(name):
    path = 'svg/ui.json'
    with open(path, 'r') as file:
        data = json.load(file)

    for i,element in enumerate(data['blocks']):
        if element['name'] == name:
            print(element)
            del data['blocks'][i]
            # del data['blocks'][i]
            print(f"Deleted block {name} from UI file")
            with open(path, 'w') as file:
                json.dump(data, file, indent=4)
            return

    print(f"⚠️ Block {name} not found in UI file")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="The name of the block to delete")
    args = parser.parse_args()

    # ask for confirmation
    confirmation = input(f"Are you sure you want to delete block {args.name} from block list? (y/n) ")

    if confirmation == 'y':
        # print("\n")
        # delete_from_block_list(args.name)
        # print("\n")
        # delete_from_help_languages(args.name)
        # print("\n")
        # delete_from_block_description_language(args.name)
        # print("\n")
        # delete_from_code_files(args.name)
        print("\n")
        delete_from_ui(args.name)
    else:
        print("Block deletion cancelled")   