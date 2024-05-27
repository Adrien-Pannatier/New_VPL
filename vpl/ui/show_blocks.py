"""
Author: Adrien Pannatier
Date of Creation: 17.05.2024
Description: you can use this script to display all the blocks in the block list. 
              command: python show_blocks.py
"""

import json

def display_block_list():
    print("\nBlocks in block list:\n")
    with open('svg/block-list.json', 'r') as file:
        data = json.load(file)
        
    for key in data.keys():
        for item in data[key]:
            print(item)


if __name__ == "__main__":
    display_block_list()
    print("\n")