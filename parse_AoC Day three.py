from itertools import chain
from read_d3_file import get_dicts


def check_rng(start, finish, chk):
    return chk in range(start-1, finish+2)
    

def check_adj(start, finish, chk):
    return (chk == start - 1) or (chk == finish + 1)
    

nums_dict, syms_dict = get_dicts('AoC Day Three Data.txt')
good_nums = []

cr = check_rng
ca = check_adj

for k, v in nums_dict.items():
    for nv in v:
        s, f, val = nv
        
        test = []
        
        # same line
        test.append([ca(s, f, sym) for sym in syms_dict[k]])
        
        # above 
        if k > 0:
            test.append([cr(s, f, sym) for sym in syms_dict[k-1]])
        
        # below
        if k < 9:
            test.append([cr(s, f, sym) for sym in syms_dict[k+1]])
        
        if any(list(chain(*test))):
            good_nums.append(val)



print(sum(good_nums))


# 315062 !!! 

# 316374

# 507214 **
