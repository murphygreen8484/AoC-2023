import re
from collections import defaultdict as dd


def get_dicts(file_name:str) -> tuple[dict, dict]:
    with open(file_name, 'r') as f:
        all_lines = iter(f.readlines())

    nums_dict = dd(list)
    symb_dict = dd(list)

    n_patt = r'(\d+)'
    s_patt = r'([^0-9.\n\ufeff])'

    for i, line in enumerate(all_lines):
        nums_dict[i] = []
        symb_dict[i] = []
    
        for nums in re.finditer(n_patt, line):
            nums_dict[i].append((nums.start(), nums.end()-1, int(nums.group())))
            
        for syms in re.finditer(s_patt, line):
            symb_dict[i].append(syms.start())
            
    return nums_dict, symb_dict

