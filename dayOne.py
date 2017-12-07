

def make_sum(s: str) -> int:
    '''
    return sum of numbers matching next digit in a sequence
    sequence is circular so last can match first digit
    '''
    seq = [int(d) for d, n in zip(s, s[1:]) if d == n]
    if s[0] == s[-1]:
        seq.append(int(s[0]))
    return sum(seq)


assert make_sum('1122') == 3
assert make_sum('1111') == 4
assert make_sum('1234') == 0
assert make_sum('91212129') == 9



