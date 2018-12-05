#!/usr/bin/python3
import string

with open('input', 'r') as fd:
    polymer = list(fd.readline()[:-1])
    
    loop = True
    current = polymer
    while loop:
        loop = False
        for i in range(1, len(current)):
            if ord(current[i-1]) == ord(current[i]) - 32 or ord(current[i-1]) == ord(current[i]) + 32:
                current.pop(i)
                current.pop(i-1)
                loop = True
                break
    print(f'{len(current)} units remain after fully reacting the polymer.')
    
    lowest = len(polymer)
    unit = None
    for M, m in zip(string.ascii_uppercase, string.ascii_lowercase):
        if (M or m) in polymer:
            current = [value for value in polymer if value != M and value != m]
            #print(current)
            loop = True
            while loop:
                loop = False
                for i in range(1, len(current)):
                    if ord(current[i-1]) == ord(current[i]) - 32 or ord(current[i-1]) == ord(current[i]) + 32:
                        current.pop(i)
                        current.pop(i-1)
                        loop = True
                        break
            if len(current) <= lowest:
                lowest = len(current)
                unit = m
    print(f'After removing all \'{unit}\' units and reacting the new polymer, {lowest} units remain.')
