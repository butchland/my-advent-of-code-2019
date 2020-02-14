#!/usr/bin/env python3
# puzzle1.py - day2 advent of code, part 1

"""
>>> int_code([])
current exceeded program length :  0
contents:  []
[]
>>> int_code([99])
[99]
>>> int_code([1,5,6,3,99,10,20])
[1, 5, 6, 30, 99, 10, 20]
>>> int_code([2,5,6,3,99,10,20])
[2, 5, 6, 200, 99, 10, 20]
>>> input1 = [1,9,10,3,2,3,11,0,99,30,40,50]
>>> int_code(input1)
[3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
>>> int_code([1,0,0,0,99])
[2, 0, 0, 0, 99]
>>> int_code([2,3,0,3,99])
[2, 3, 0, 6, 99]
>>> int_code([2,4,4,5,99,0])
[2, 4, 4, 5, 99, 9801]
>>> int_code([1,1,1,4,99,5,6,0,99])
[30, 1, 1, 4, 2, 5, 6, 0, 99]

>>> input1202 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]
>>> input1202[1] = 12
>>> input1202[2] = 2
>>> result = int_code(input1202)
>>> result[0]
4570637
>>> noun_verb(12,2)
4570637
"""

# Here are the initial and final states of a few more small programs:

#     1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
#     2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
#     2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
#     1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
# To do this, before running the program, replace position 1 with the value 12 
#  and replace position 2 with the value 2. What value is left at position 0 after the program halts?

INPUT_1202 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]

def noun_verb(noun:int, verb:int, input:list = INPUT_1202) -> int:
    output = input.copy()
    output[1] = noun
    output[2] = verb
    result = int_code(output)
    return result[0]

def is_invalid(value: int, input:list) -> bool:
    return value < 0 or value >= len(input)

def int_code(input: list, current: int = 0) -> list:
    output = input.copy()
    while True:
        if current >= len(output):
            print("current exceeded program length : ", current)
            print("contents: ", output)
            break
        current_opcode = output[current]
        if current_opcode == 1:
            op_address1 = output[current+1]
            if is_invalid(op_address1, output):
                print("invalid address1 ", op_address1, " at current ", current)
                print("contents: ", output)
                break
            op_address2 = output[current+2]
            if is_invalid(op_address2, output):
                print("invalid address2 ", op_address2, " at current ", current)
                print("contents: ", output)
                break
            op_address3 = output[current+3]
            if is_invalid(op_address3, output):
                print("invalid address3 ", op_address3, " at current ", current)
                print("contents: ", output)
                break
            output[op_address3] = output[op_address1] + output[op_address2]
        elif current_opcode == 2:
            op_address1 = output[current+1]
            if is_invalid(op_address1, output):
                print("invalid address1 ", op_address1, " at current ", current)
                print("contents: ", output)
                break
            op_address2 = output[current+2]
            if is_invalid(op_address2, output):
                print("invalid address2 ", op_address2, " at current ", current)
                print("contents: ", output)
                break
            op_address3 = output[current+3]
            if is_invalid(op_address3, output):
                print("invalid address3 ", op_address3, " at current ", current)
                print("contents: ", output)
                break
            output[op_address3] = output[op_address1] * output[op_address2]
        elif current_opcode == 99:
            break
        else:
            print("Error: unknown opcode ", output[current], "at address ", current)
            break
        current += 4
    return output

if __name__ == "__main__":
    import doctest
    doctest.testmod()
