import numpy as np
import re

def Add(string):
    if string == '':
        return 0
    delim = ',|\n'
    n_list = np.array(re.split(delim,string), dtype=np.float32)
    if len(n_list) == 1:
        return n_list
    elif len(n_list) == 2:
        return (n_list[0] + n_list[1])
    else:
        return (n_list[0] + n_list[1] + n_list[2])

