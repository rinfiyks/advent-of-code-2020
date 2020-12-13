from common import read_file, timer
from math import gcd


@timer
def part_1():
    I = read_file('day13')
    ts = int(I[0])
    buses = [int(x) for x in I[1].split(',') if x != 'x']
    times = [b - (ts % b) for b in buses]
    val, i = min((v, i) for (i, v) in enumerate(times))
    print(buses[i] * val)


@timer
def part_2():
    I = read_file('day13')
    ids = [i for (i,v) in enumerate(I[1].split(',')) if v != 'x']
    buses = [int(x) for x in I[1].split(',') if x != 'x']

    offsets = []
    for i in range(len(ids)):
        offsets.append(buses[i] + (ids[i]//buses[i] * buses[i]) - ids[i])

    current = buses[0]
    for i in range(1, len(buses)):
        inc = lcm(buses[:i])
        while current % buses[i] != offsets[i]:
            current += inc

    print(current)


def lcm(l):
    lcm = l[0]
    for i in l[1:]:
        lcm = lcm*i//gcd(lcm, i)
    return lcm


part_1()
part_2()
