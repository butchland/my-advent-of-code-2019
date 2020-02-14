#!/usr/bin/env python3
# puzzle2.py - day 1 advent of code, part 2

"""
>>> revised_fuel_for_mass(14)
2
>>> revised_fuel_for_mass(1969)
966
>>> revised_fuel_for_mass(100756)
50346
>>> fuel_counter_upper()
4998585
"""

# A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, 
# which would call for a negative fuel), so the total fuel required is still just 2.

# At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 
# 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. 
# So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.

# The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

from puzzle1 import fuel_for_mass

def revised_fuel_for_mass(mass:int) -> int:
    fuel_mass = fuel_for_mass(mass)
    if fuel_mass <= 0:
        return 0
    return fuel_mass + revised_fuel_for_mass(fuel_mass)

def fuel_counter_upper(file_name:str = "puzzle1.input") -> int:
    total_fuel = 0
    with open(file_name) as fp:
        for line in fp:
            total_fuel += revised_fuel_for_mass(int(line))
    return total_fuel


if __name__ == "__main__":
    import doctest
    doctest.testmod()
