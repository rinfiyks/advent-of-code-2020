from common import read_file, timer
import re


@timer
def part_1():
    I = read_file('day2')

    count = 0
    for l in I:
        r = re.search(r'^(\d*)-(\d*) (.): (.*)', l)
        lower = int(r[1])
        upper = int(r[2])
        c = r[3]
        passwd = r[4]
        n = passwd.count(c)
        if (n >= lower and n <= upper):
            count += 1

    print(count)

@timer
def part_2():
    I = read_file('day2')

    count = 0
    for l in I:
        r = re.search(r'^(\d*)-(\d*) (.): (.*)', l)
        first = int(r[1])
        second = int(r[2])
        c = r[3]
        passwd = r[4]
        if ((passwd[first - 1] == c) ^ (passwd[second - 1] == c)):
            count += 1

    print(count)


part_1()
part_2()
