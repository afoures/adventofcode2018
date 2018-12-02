#!/usr/bin/python3

with open('input', 'r') as fd:
    lines = fd.readlines()
    
    two = 0
    three = 0
    for line in lines:
        tmp1, tmp2 = 0,0
        for char in line:
            if line.count(char) == 2:
                tmp1 = 1
            if line.count(char) == 3:
                tmp2 = 1
        two += tmp1
        three += tmp2
    result = two * three
    print(f'The checksum is {result}.')

    for x in range(len(lines)):
        for y in range(x, len(lines)):
            check = 0
            pos = 0
            for i in range(len(lines[x])):
                if lines[x][i] != lines[y][i]:
                    check += 1
                    pos = i
            if check == 1:
                tmp = lines[x][:pos] + lines[x][pos+1:-1]
                print(f'Box IDs letters in common "{tmp}".')
