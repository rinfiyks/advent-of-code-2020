from common import read_file, timer
import copy


@timer
def part_1():
    I = read_file('day11')
    grid = [list(x) for x in I]
    n = 0
    while True:
        next_grid = step1(grid)
        n +=1
        if next_grid == grid:
            break
        grid = next_grid
    print(count_occ(grid))


@timer
def part_2():
    I = read_file('day11')
    grid = [list(x) for x in I]
    n = 0
    while True:
        next_grid = step2(grid)
        n +=1
        if next_grid == grid:
            break
        grid = next_grid
    print(count_occ(grid))


def step1(grid):
    next_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            c = adj_occ1(grid, j, i)
            seat = grid[i][j]
            if seat == 'L' and c == 0:
                next_grid[i][j] = '#'
            elif seat == '#' and c >= 4:
                next_grid[i][j] = 'L'
    return next_grid


def step2(grid):
    next_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            c = adj_occ2(grid, j, i)
            seat = grid[i][j]
            if seat == 'L' and c == 0:
                next_grid[i][j] = '#'
            elif seat == '#' and c >= 5:
                next_grid[i][j] = 'L'
    return next_grid


def adj_occ1(grid, x, y):
    c = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i >= 0 and j >= 0 and not (i == x and j == y) and i < len(grid[0]) and j < len(grid):
                if grid[j][i] == '#': c += 1
    return c


def adj_occ2(grid, x, y):
    c = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0: continue
            i=x+di
            j=y+dj
            while i >= 0 and j >= 0 and i < len(grid[0]) and j < len(grid):
                if grid[j][i] == '.':
                    i+=di
                    j+=dj
                    continue
                else:
                    if grid[j][i] == '#': c += 1
                    break

    return c


def print_g(grid):
    for i in grid:
        print(''.join(i))
    print()


def count_occ(grid):
    return sum(x.count('#') for x in grid)


part_1()
part_2()
