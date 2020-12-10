from common import read_file, timer


@timer
def part_1():
    input_data = sorted([int(x) for x in read_file('day10')])
    c1 = 0
    c3 = 1
    prev = 0
    for i in input_data:
        diff = i - prev
        if diff == 1: c1 += 1
        elif diff == 3: c3 += 1
        prev = i

    print(c1*c3)


@timer
def part_2():
    input_data = sorted([int(x) for x in read_file('day10')])
    I = [0] + input_data + [max(input_data) + 3]
    ways = [0] * len(I)
    ways[0] = 1
    for i in range(1, len(I)):
        n = 0
        for j in range(1, 4):
            if (I[i] - I[i-j] < 4): n += ways[i-j]
        ways[i] = n
    print(ways[-1])


part_1()
part_2()
