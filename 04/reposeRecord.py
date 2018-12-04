#!/usr/bin/python3
import re

with open('input', 'r') as fd:
    lines = fd.readlines()
    lines.sort()
    
    guards = []
    index = -1
    for line in lines:
        number = re.search(r'#(\d*) ', line)
        if number:
            for i in range(len(guards)):
                if guards[i][0] == int(number.group(1)):
                    index = i
                    break
                else:
                    index = -1
            if index == -1:
                guards.append([int(number.group(1))])
        time = re.search(r'\d*:\d*', line)
        if 'asleep' in line:
            guards[index].append(time.group(0))
        if 'wakes' in line: 
            guards[index].append(time.group(0))
    
    graph = [[0 for _ in range(60)] for _ in range(len(guards))]
    total_sleep = [0 for _ in range(len(guards))]
    for index, guard in enumerate(guards):
        sleep = guard[1:]
        for x in range(len(sleep)//2):
            tmp1 = sleep[x*2].split(':')[1]
            tmp2 = sleep[x*2+1].split(':')[1]
            for i in range(int(tmp1), int(tmp2)):
                total_sleep[index] += 1
                graph[index][i] += 1
                
    print(f' Total sleep for each guards -> {total_sleep}')

    most_asleep = total_sleep.index(max(total_sleep))
    ID = guards[most_asleep][0]
    minute = graph[most_asleep].index(max(graph[most_asleep]))

    graph = [[x for x in range(60)]] + graph
    guards = ['.'] + guards
    print('graph:\n'+'\n'.join([''.join(['{:^4}'.format(item) for item in ([guards[i][0]] + row)]) for i, row in enumerate(graph)]))
    graph.pop(0)
    guards.pop(0)

    print(f'Strategy 1: ID({ID}) at {minute} minute. Result is {minute * ID}.')

    each_max = list(map(max, graph))
    the_max = max(each_max)
    most_asleep = each_max.index(the_max)
    ID = guards[most_asleep][0]
    minute = graph[most_asleep].index(max(graph[most_asleep]))
    
    print(f'Strategy 2: ID({ID}) at {minute} minutes. Result is {minute * ID}.')

    
        
