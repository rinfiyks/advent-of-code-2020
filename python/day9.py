from common import read_file, timer


@timer
def part_1():
    I = [int(x) for x in read_file('day9')]
    prev = I[:25]

    for i in range(25, len(I)):
        x = I[i]
        if not sum_exists(prev, x):
            print(x)
            break
        prev = prev[1:] + [x]



def sum_exists(p, n):
    for i in p:
        for j in p:
            if i + j == n and i != j: return True
    return False


@timer
def part_2():
    I = [int(x) for x in read_file('day9')]
    n = 258585477
    w = 2
    while True:
        for i in range(0, len(I) - w):
            if sum(I[i:i+w]) == n:
                r = I[i:i+w]
                print(min(r) + max(r))
                return
        w += 1



part_1()
part_2()
