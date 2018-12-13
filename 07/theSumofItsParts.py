#!/usr/bin/python3
import copy

with open('input', 'r') as fd:
    lines = fd.readlines()
    instructions = []
    for line in lines:
        tmp = line.split(' ')
        instructions.append(tuple(tmp[1]+ tmp[7]))

    tasks = {}
    for instruction in instructions:
        for i, name in enumerate(instruction):
            if name not in tasks:
                tasks[name] = [0, tuple()]
            if i == 1:
                tasks[name][0] += 1
                tasks[old][1] += tuple(name)
            else:
                old = name
    #print(tasks)
    tasks_save = copy.deepcopy(tasks)
    
    queue = []
    for name in tasks:
        if tasks[name][0] == 0:
            queue += [name]

    order = []
    while len(queue) > 0:
        queue.sort()
        #print(queue)
        current = queue[0]
        tasks[current][0] -= 1
        if tasks[current][0] <= 0:
            order += [current]
            tmp = list(tasks[current][1])
            queue += tmp
        queue.remove(current)
    print('The steps are '+''.join(f'{x}' for x in order) + '.')

    tasks = tasks_save
    for name in tasks:
        if tasks[name][0] == 0:
            queue += [name]

    time = 0
    worker = []

    # Add some help for this part
    def addWorker():
        global queue
        while len(worker) < 5 and queue:
            x = min(queue)
            queue = [y for y in queue if y!=x]
            worker.append((time+61+ord(x)-ord('A'), x))

    addWorker()
    while queue or worker:
        time, x = min(worker)
        worker = [y for y in worker if y!=(time,x)]
        for i in tasks[x][1]:
            tasks[i][0] -=1
            if tasks[i][0] == 0:
                queue.append(i)
        addWorker()
            
    print(f'It will take {time} seconds to complete all the steps with 5 workers')
