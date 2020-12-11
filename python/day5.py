from common import read_file, timer


@timer
def part_1():
    I = read_file('day5')
    print(max([seat_id(l) for l in I]))


@timer
def part_2():
    I = read_file('day5')
    seats = sorted([seat_id(l) for l in I])
    for i in range(seats[0], seats[-1]):
        if (i - 1 in seats and i + 1 in seats and i not in seats):
            print(i)
            break


def seat_id(bp):
    row = bp[:7]
    col = bp[7:]
    row_id = int(row.replace('F', '0').replace('B', '1'), 2)
    col_id = int(col.replace('L', '0').replace('R', '1'), 2)
    return row_id * 8 + col_id


part_1()
part_2()
