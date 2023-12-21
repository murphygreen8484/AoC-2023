""" Useful functions to parse through dictionary of numbers and symbol locations.
    For use in the Day 3 AoC coding challenge """


def check_ranges(start_num: int, end_num: int, chk_vals: list[int]) -> bool:
    """ Takes in two int arguments, and one list of ints. Then creates a range
      object and checks if any of the ints in the list are in the ragne.
      If yes, return True, if not, return False """

    assert end_num >= start_num

    # minus one from the start and add one to the end to account for diagonals
    # plus an additonal one at the end as range() is not inclusive
    rng_obj = range(start_num - 1, end_num + 2)

    for chk in chk_vals:
        if chk in rng_obj:
            return True

    return False


def check_adjacent(start_num: int, end_num: int, chk_vals: list[int]) -> bool:
    """ Takes in two int arguments and one list of ints. Checks the list of ints
    against the starting value minus one and the ending value plus one to check
    if it is adjacent. If yes, return True, if not, return False """

    assert end_num >= start_num

    for chk in chk_vals:
        if (chk == start_num - 1) or (chk == end_num + 1):
            return True

    return False
