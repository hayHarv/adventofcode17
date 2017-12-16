'''
http://adventofcode.com/2017/day/3
'''
import numpy as np
from math import sqrt

def taxicab(p: np.array, q: np.array) -> int:
    '''
    p : vector of coordinates point a
    q : vector of coordinates point b
    '''
    return np.sum(np.abs(p - q))



def last_digit(nth_box: int):
    d = 2
    n = nth_box
    a_n = 1 + ((n-1)*d)
    return a_n ** 2

def find_previous(x):
    '''
    return last values for each box < x
    e.g. 
    find_previous(10)
    1, 9
    '''
    a = np.arange(1, x+1)
    asqrt = np.sqrt(a)
    b = a[((a-1)%8 ==0) & (asqrt - asqrt.astype(int)== 0)]
    return b


def which_box(x):
    if x == 1:
        return 1
    else:
        return len(find_previous(x))+1

#TODO find coordinates
#TODO check for efficiency on find_previous...seems shitty

if __name__=="__main__":
    assert which_box(10) == 3
    assert which_box(26) == 4
