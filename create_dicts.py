import re
from typing import Pattern, Dict, List, Tuple


def create_dict_rngs(file_name: str, reg_patt: Pattern[str]) -> Dict[int, List[Tuple[int, int, int]]]:
    """ reads a text file line by line creating a dictionary of found value ranges based on a re pattern.
        The dictionary has the line number as the key (starting with 1), and the first two ints in the tuple
        being the start and end of the span of the found value, and the third int being the value itself.
        The Pattern is a regex string pattern. """

    with open(file_name, 'r') as f:
        data = iter(f.readlines())

    rng_dict = dict()

    for no, line in enumerate(data, 1):
        rng_dict[no] = []
        for vals in re.finditer(reg_patt, line):
            rng_dict[no].append((vals.start(), vals.end() - 1, int(vals.group())))

    return rng_dict


def create_dict_pnt(file_name: str, reg_patt: Pattern[str]) -> Dict[int, List[int]]:
    """ reads a text file line by line creating a dictionary of found value ranges based on a re pattern.
        The dictionary has the line number as the key (starting with 1), with the values be lists of
        starting locations of found values (the values themselves are not returned).
        The Pattern is a regex string pattern. """

    with open(file_name, 'r') as f:
        data = iter(f.readlines())

    pnt_dict = dict()

    for no, line in enumerate(data, 1):
        pnt_dict[no] = []
        for vals in re.finditer(reg_patt, line):
            pnt_dict[no].append(vals.start())

    return pnt_dict
