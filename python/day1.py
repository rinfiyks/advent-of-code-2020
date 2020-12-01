from common import read_file, timer


@timer
def part_1():
    input_data = read_file('day1')
    input_data = [int(i) for i in input_data]
    offsets = [2020 - i for i in input_data]
    combined = input_data + offsets
    duplicates = list(set([i for i in combined if combined.count(i) > 1]))
    print(duplicates[0] * duplicates[1])


@timer
def part_2():
    input_data = read_file('day1')
    input_data = [int(i) for i in input_data]
    offsets = [2020 - i for i in input_data]
    two_combined = [[i, j] for i in input_data for j in input_data if i + j < 2020 and i != j]
    for i in two_combined:
        if ((i[0] + i[1]) in offsets):
            print(i[0] * i[1] * (2020 - i[0] - i[1]))
            break


part_1()
part_2()
