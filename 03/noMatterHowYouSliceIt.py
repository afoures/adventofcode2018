#!/usr/bin/python3

with open('input', 'r') as fd:
    lines = fd.readlines()
    claims = []
    for line in lines:
        line = line.split('@')[1]
        tmp = line.split(':')
        start = tmp[0].split(',')
        size = tmp[1].split('x')
        claim = list(map(int, start + size))
        claims.append(claim)

    fabric = [['.' for x in range(1000)] for y in range(1000)]
    for index, claim in enumerate(claims):
        for y in range(claim[1], claim[1] + claim[3]):
            for x in range(claim[0], claim[0] + claim[2]):
                if fabric[y][x] == '.':
                    fabric[y][x] = index
                else:
                    fabric[y][x] = '#'

    total = 0
    for i in range(1000*1000):
        if fabric[i//1000][i%1000] == '#':
            total += 1
    
    print(f'There is a total of {total} inches overlapping')
    
    non_overlapping = None
    for index, claim in enumerate(claims):
        overlap = 0
        for index2, tmp in enumerate(claims):
            if index != index2:
                width = min(claim[0] + claim[2], tmp[0] + tmp[2])
                width -= max(claim[0], tmp[0])
                height = min(claim[1] + claim[3], tmp[1] + tmp[3])
                height -= max(claim[1], tmp[1])
                if height > 0 and width > 0:
                    overlap = 1
        if overlap == 0:
            non_overlapping = index + 1
            break
    print(f'The claim {non_overlapping} doen\'t overlap')
