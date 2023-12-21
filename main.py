""" Main code to create dictionaries of the found numbers and symbols and then check them against
    each other. Two helper files create to store the functions used for parsing. Code to be used for
    solving the AoC Day 3 puzzle """

import re

from create_dicts import create_dict_pnt
from create_dicts import create_dict_rngs
from parse_dicts import check_ranges as cr
from parse_dicts import check_adjacent as ca


nums_patt = re.compile(r'(\d+)')
syms_patt = re.compile(r'([^0-9.\n])')

def main(text_path: str) -> None:
    """ returns a list of all the found ints """

    matched_nums = []
    nums_dict = create_dict_rngs(text_path, nums_patt)
    symb_dict = create_dict_pnt(text_path, syms_patt)

    assert len(nums_dict.keys()) == len(symb_dict.keys())

    for line, vals in nums_dict.items():
        for nums_tup in vals:
            found = False
            start_num, end_num, val_num = nums_tup

            # check same row
            if ca(start_num, end_num, symb_dict[line]):
                found = True
            # check above
            if line > 1 and not found:
                if cr(start_num, end_num, symb_dict[line - 1]):
                    found = True

            # check below
            if line < len(nums_dict.keys()) and not found:
                if cr(start_num, end_num, symb_dict[line + 1]):
                    found = True

            if found:
                matched_nums.append(val_num)

    print(sum(matched_nums))


if __name__ == '__main__':

    live_file_path = 'AoC Day Three Data.txt'
    test_file_path = 'AoC Day Three Test Data.txt'

    main(live_file_path)
