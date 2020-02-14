#!/usr/bin/env python3
# puzzle1.py - day 1 advent of code, part 1

"""
>>> 12/3 
4.0
>>> int(_)
4
>>> _ - 2
2
>>> fuel_for_mass(12)
2
>>> 14/3
4.666666666666667
>>> int(14/3)
4
>>> fuel_for_mass(14)
2
>>> fuel_for_mass(1969)
654
>>> fuel_for_mass(100756)
33583
>>> fuel_counter_upper()
3334282
"""

# Compute fuel for mass
# For example:
#     For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
#     For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
#     For a mass of 1969, the fuel required is 654.
#     For a mass of 100756, the fuel required is 33583.
# from AOC https://adventofcode.com/2019/day/1

def fuel_for_mass(mass : int) -> int:
    return int(mass/3.0) - 2

def fuel_counter_upper(file_name:str="puzzle1.input") -> int:
    total_fuel = 0
    with open(file_name) as fp:
        for line in fp:
            total_fuel += fuel_for_mass(int(line))
    return total_fuel


if __name__ == "__main__":
    import doctest
    doctest.testmod()
