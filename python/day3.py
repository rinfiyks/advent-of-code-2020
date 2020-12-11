from common import read_file, timer


@timer
def part_1():
    I = read_file('day3')
    x_pos = 0
    width = len(I[0])
    count = 0
    for row in I:
        if row[x_pos] == '#':
            count += 1
        x_pos = (x_pos + 3) % width
    print(count)


@timer
def part_2():
    I = read_file('day3')
    s1 = slope(I, 1, 1)
    s2 = slope(I, 1, 3)
    s3 = slope(I, 1, 5)
    s4 = slope(I, 1, 7)
    s5 = slope(I, 2, 1)
    print(s1*s2*s3*s4*s5)


def slope(d, x, y):
    x_pos = 0
    width = len(d[0])
    count = 0
    for i in range(0, len(d), x):
        row = d[i]
        if row[x_pos] == '#':
            count += 1
        x_pos = (x_pos + y) % width
    return count


part_1()
part_2()
