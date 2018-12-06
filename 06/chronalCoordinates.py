#!/usr/bin/python3

with open('input', 'r') as fd:
    lines = fd.readlines()
    coordinates = []
    max_x = 0
    max_y = 0
    for line in lines:
        line = line[:-1]
        coordinates.append(tuple(map(int, line.split(','))))
        max_x = coordinates[-1][0] if max_x < coordinates[-1][0] else max_x
        max_y = coordinates[-1][1] if max_y < coordinates[-1][1] else max_y

    grid = [['.' for _ in range(max_x + 2)] for _ in range(max_y + 2)]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            dist = (max_x+2) * (max_y+2) * 2
            for i, coordinate in enumerate(coordinates):
                tmp = abs(x - coordinate[0]) + abs(y - coordinate[1])
                if tmp <= dist:
                    value = chr(65+i) if tmp < dist else '.'
                    dist = tmp
                    grid[y][x] = value

    largest_area = 0
    index_largest_area = 0
    for i in range(len(coordinates)):
        brk = 0
        current_area = 0
        for y, row in enumerate(grid):
            if (y == 0 or y == len(grid)-1) and chr(65+i) in row:
                break
            for x, col in enumerate(row):
                if (x == 0 or x == len(row)-1) and col == chr(65+i):
                    brk = 1
                    break
                if col == chr(65+i):
                    current_area += 1
            if brk == 1:
                break
        if current_area > largest_area:
            largest_area = current_area
            index_largest_area = i

    grid2 = [['.' for _ in range(max_x + 2)] for _ in range(max_y + 2)]
    size = 0
    for y in range(len(grid2)):
        for x in range(len(grid2[y])):
            tmp = 0
            for i, coordinate in enumerate(coordinates):
                tmp += abs(x - coordinate[0]) + abs(y - coordinate[1])
            if tmp < 10000:
                value = '#'
                grid2[y][x] = value
                size += 1

    #print('grid:\n'+'\n'.join([''.join(['{:^2}'.format(item) for item in row]) for row in grid]))
    print(f'Size of largest finite area : {largest_area}.')
    #print(chr(65+index_largest_area))
    #print('grid:\n'+'\n'.join([''.join(['{:^2}'.format(item) for item in row]) for row in grid2]))
    print(f'Size of the region with all locations wich have a total distance to all given coordinates of less than 10000 : {size}.')

