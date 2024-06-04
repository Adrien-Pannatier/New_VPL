"""
Author: Adrien Pannatier
Date of Creation: 30.05.2024
Description: This script allows you to edit vpl blocks in a easier way
             Commands:
             - python edit_block.py -h
             - python edit_block.py show_blocks
             - python edit_block.py delete_block [block_name]
"""

import json
import argparse

# DISPLAY BLOCKS ======================================================================================================================

def display_block_list():
    print("\nBlocks in block list:\n")
    with open('svg/block-list.json', 'r') as file:
        data = json.load(file)
        
    for key in data.keys():
        for item in data[key]:
            print(item)

    print("\n")

# DELETE BLOCKS =======================================================================================================================

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

    for lang in code_languages:
        delete = False
        path = f'svg/{lang}.json'
        with open(path, 'r') as file:
            data = json.load(file)

        for i,element in enumerate(data['blocks']):
            if element['name'] == name:
                try: 
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
            del data['blocks'][i]
            print(f"Deleted block {name} from UI file")
            with open(path, 'w') as file:
                json.dump(data, file, indent=4)
            return

    print(f"⚠️ Block {name} not found in UI file")

# ADD BLOCKS ==========================================================================================================================

def add_block():
    name = input("Enter block name: ")
    add_block_to_block_list(name)
    add_block_to_help_languages(name)
    add_block_to_block_description_language(name)

def add_block_to_block_list(name):
    with open('svg/block-list.json', 'r') as file:
        data = json.load(file)
        
    for key in data.keys():
        for item in data[key]:
            if item == name:
                print(f"⚠️ Block {name} already in block list")
                return

    data['blocks'].append(name)
    with open('svg/block-list.json', 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Added block {name} to block list")

def add_block_to_help_languages(name):
    languages = ["de", "en", "fr", "it"]
    for lang in languages:
        path = f'svg/help-blocks-{lang}.json'
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        
        for element in data['help'][lang]['blocks']:
            if element == name:
                print(f"⚠️ Block {name} already in {lang} help file")
                continue

        data['help'][lang]['blocks'][name] = [f"ADD DESCRIPTION HERE in {lang}"]
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Added block {name} to {lang} help file")

def add_block_to_block_description_language(name):
    languages = ["de", "en", "fr", "it"]
    for lang in languages:
        path = f'svg/block-{lang}.json'
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)

        for element in data['i18n'][lang]:
            if element == name:
                print(f"⚠️ Block {name} already in {lang} description file")
                continue

        data['i18n'][lang][name] = f"ADD DESCRIPTION HERE in {lang}"
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Added block {name} to {lang} description file")           

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage block list: display blocks or delete a block")
    subparsers = parser.add_subparsers(dest="command")

    # Sub-parser for the show_blocks command
    show_parser = subparsers.add_parser("show_blocks", help="Display all blocks in the block list")

    # Sub-parser for the delete_block command
    delete_parser = subparsers.add_parser("delete_block", help="Delete a block from the block list")
    delete_parser.add_argument("name", help="The name of the block to delete")

    args = parser.parse_args()

    if args.command == "show_blocks":
        display_block_list()
    elif args.command == "delete_block":
        # Ask for confirmation
        confirmation = input(f"Are you sure you want to delete block {args.name} from block list? (y/n) ")
        if confirmation.lower() == 'y':
            delete_from_block_list(args.name)
            delete_from_help_languages(args.name)
            delete_from_block_description_language(args.name)
            delete_from_code_files(args.name)
            delete_from_ui(args.name)
        else:
            print("Block deletion cancelled")
    else:
        parser.print_help()
