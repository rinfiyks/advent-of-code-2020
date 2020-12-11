from common import read_file, timer


@timer
def part_1():
    I = read_file('day8')
    i = 0
    acc = 0
    visited = set()
    while True:
        if i in visited:
            break
        else:
            instr = I[i][:3]
            val = int(I[i][4:])

            visited.add(i)
            if instr == 'acc':
                acc += val
                i += 1
            elif instr == 'jmp':
                i += val
            else:
                i += 1

    print(acc)


@timer
def part_2():
    I = read_file('day8')

    for i in range(len(I)):
        l = I.copy()
        if l[i][:3] == 'nop':
            l[i] = 'jmp' + l[i][3:]
        if l[i][:3] == 'jmp':
            l[i] = 'nop' + l[i][3:]
        
        looped = False
        i = 0
        acc = 0
        visited = set()
        while i < len(l):
            if i in visited:
                looped = True
                break
            else:
                instr = l[i][:3]
                val = int(l[i][4:])

                visited.add(i)
                if instr == 'acc':
                    acc += val
                    i += 1
                elif instr == 'jmp':
                    i += val
                else:
                    i += 1
        if not looped:
            print(acc)


part_1()
part_2()
