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
        max_val = 1
        box = 1
        return box
    else:
        previous = find_previous(x)
        max_val = max(previous)
        box = len(previous) +1
        return box

def sidelength(nth_box):
    return last_digit(nth_box)**.5

def start_coords(x):
    base = (which_box(x))-1
    x_coord = base
    y_coord = base*-1
    return [x_coord, y_coord]


def squares_in_box(nth_box):
    sidelens = sidelength(nth_box)
    return int((sidelens*4)-4)

def midsides(x):
    a = which_box(x) -1
    a_zero = pow(a*2 -1, 2)
    return a, [a_zero + x * a for x in [1,3,5,7]]

def distance(x):
    a, centers = midsides(x)
    return a + min([abs(x - i) for i in centers])

def next_coordinates(x, y):
    if x == y == 0: return (1,0)
    if y > -x and x > y: return (x, y+1)
    if y > -x and y >= x: return(x-1, y)
    if y <= -x and x < y : return (x, y-1)
    if y <= -x and x >= y: return(x+1, y)


if  __name__=="__main__":
    assert which_box(10) ==  3
    assert which_box(26) ==  4
    assert last_digit(2) == 9
    assert sidelength(2) == 3
    assert sidelength(1) == 1
    assert start_coords(10) == [2, -2]
    assert start_coords(1) == [0,0]
