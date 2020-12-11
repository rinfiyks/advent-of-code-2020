from common import read_file, timer


@timer
def part_1():
    I = read_file('day1')
    I = [int(i) for i in I]
    offsets = [2020 - i for i in I]
    combined = I + offsets
    duplicates = list(set([i for i in combined if combined.count(i) > 1]))
    print(duplicates[0] * duplicates[1])


@timer
def part_2():
    I = read_file('day1')
    I = [int(i) for i in I]
    offsets = [2020 - i for i in I]
    two_combined = [[i, j] for i in I for j in I if i + j < 2020 and i != j]
    for i in two_combined:
        if ((i[0] + i[1]) in offsets):
            print(i[0] * i[1] * (2020 - i[0] - i[1]))
            break


part_1()
part_2()
