#!/usr/bin/python3

with open('input', 'r') as fd:
    lines = fd.readlines()

    frequency = 0
    for line in lines:
        frequency += int(line)
    print(f'Frequency after changes: {frequency}.')

    frequency = 0
    already_reached = [0]
    loop = True
    while loop:
        for line in lines:
            frequency += int(line)
            if frequency in already_reached:
                loop = False
                break
            already_reached.append(frequency)
    print(f'First reaches {frequency} twice.')
