#!/usr/bin/env python3
# puzzle1.py - day2 advent of code, part 1

"""
>>> find_noun_verb_for_result(4570637)
(12, 2)
>>> find_noun_verb_for_result()
(54, 85)
>>> output_expected(4570637)
1202
>>> output_expected()
5485
"""
from puzzle1 import noun_verb

EXPECTED_RESULT = 19690720
def find_noun_verb_for_result(expect:int=EXPECTED_RESULT) -> (int,int):
    for noun in range(100):
        for verb in range(100):
            result = noun_verb(noun,verb)
            if result == expect:
                return (noun,verb)
    return (-1,-1)

def output_expected(expect:int=EXPECTED_RESULT) -> int:
    result = find_noun_verb_for_result(expect)
    return result[0]*100 + result[1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
