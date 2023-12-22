# AoC Day 3 Challenge

## Description
This code is designed to solve the Advent of Code Day 3 puzzle. It utilizes functions to parse through dictionaries of numbers and symbols, checking for specific patterns.

## Files

### 1. create_dicts.py
Contains functions to create dictionaries of found value ranges and starting locations based on a regex pattern.

#### `create_dict_rngs(file_name: str, reg_patt: Pattern[str]) -> Dict[int, List[Tuple[int, int, int]]]:`
Reads a text file line by line, creating a dictionary of found value ranges based on a regex pattern. The dictionary has the line number as the key, with the first two ints in the tuple being the start and end of the span of the found value, and the third int being the value itself.

#### `create_dict_pnt(file_name: str, reg_patt: Pattern[str]) -> Dict[int, List[int]]:`
Reads a text file line by line, creating a dictionary of found value ranges based on a regex pattern. The dictionary has the line number as the key, with the values being lists of starting locations of found values.

### 2. parse_dicts.py
Contains helper functions to check ranges and adjacency for a given set of numbers.

#### `check_ranges(start_num: int, end_num: int, chk_vals: list[int]) -> bool:`
Takes in two int arguments and one list of ints. Creates a range object and checks if any of the ints in the list are in the range. Returns True if yes, False if not.

#### `check_adjacent(start_num: int, end_num: int, chk_vals: list[int]) -> bool:`
Takes in two int arguments and one list of ints. Checks the list of ints against the starting value minus one and the ending value plus one to check if it is adjacent. Returns True if yes, False if not.

### 3. main_code.py
The main code to create dictionaries of found numbers and symbols, and then check them against each other to solve the AoC Day 3 puzzle.

#### `main(text_path: str) -> None:`
Returns a list of all the found ints. Reads a text file, creates dictionaries of found numbers and symbols, and checks them against each other. Prints the sum of matched numbers.

## Usage

1. Ensure you have the required input file (`AoC Day Three Data.txt`).
2. Run `main_code.py` to obtain the result.

## Dependencies
- Python 3.x

## Note
This code is specifically designed for the Advent of Code Day 3 puzzle. Ensure you have the correct input file format and adjust paths accordingly.

Feel free to modify and adapt the code as needed.
