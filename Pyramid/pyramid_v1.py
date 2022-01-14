# Constants


# Variables


# Functions

from venv import create


def get_input():
    # input
    # control input
    while True :
        blocks = int(input("Enter blocks number: "))
        if blocks in range(3, 100): break        
        pass
    return blocks

def calc_height(total_blocks):
    next_row_blocks = 0
    blocks_left = total_blocks
    current_height = 0   
    
    while blocks_left > next_row_blocks:
        # Build next row
        next_row_blocks += 1
        blocks_left -= next_row_blocks
        current_height += 1
        
        pass    
    
    return current_height


def create_pyramid(height, drew_symbol = "*", spacer_symbol = "."):
    pyramid_string = ""
    for next_row in range(1, height + 1):
        # create next row text string
        pyramid_string += (height - next_row) * spacer_symbol 
        pyramid_string += (next_row) * (drew_symbol + spacer_symbol) 
        pyramid_string += (height - next_row - 1) * spacer_symbol 
        pyramid_string += "\n"
        
    return pyramid_string


# MAIN
pyramid_total_blocks = get_input()
pyramid_height = calc_height(pyramid_total_blocks)
print (pyramid_height)  
print(create_pyramid(pyramid_height))
print(create_pyramid(pyramid_height, "^", " "))
print(create_pyramid(pyramid_height, "$", "."))
# create_pyramid()    
