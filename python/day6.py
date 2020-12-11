from common import read_file, timer


@timer
def part_1():
    I = read_file('day6')
    I.append('')

    s = ''
    count = 0
    for l in I:
        if l == '':
            count += len(set(s))
            s = ''
        else:
            s += l
    print(count)


@timer
def part_2():
    I = read_file('day6')
    I.append('')

    s = set()
    count = 0
    flag = True
    for l in I:
        if l == '':
            count += len(s)
            s = set()
            flag = True
        else:
            if flag:
                s = set(l)
                flag = False
            else:
                s = s.intersection(set(l))

    print(count)


part_1()
part_2()
