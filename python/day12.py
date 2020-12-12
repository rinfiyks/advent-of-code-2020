from common import read_file, timer


@timer
def part_1():
    I = read_file('day12')
    x = 0
    y = 0
    direc = 0
    dx=1
    dy=0
    for i in I:
        action = i[0]
        val = int(i[1:])
        if action == 'F':
            x+=val*dx
            y+=val*dy
        elif action == 'N':
            y += val
        elif action == 'S':
            y -= val
        elif action == 'W':
            x -= val
        elif action == 'E':
            x += val
        elif action == 'L':
            direc = (direc + val) % 360
        elif action == 'R':
            direc = (direc - val) % 360

        if direc == 0:
            dx=1
            dy=0
        elif direc == 90:
            dx=0
            dy=1
        elif direc == 180:
            dx=-1
            dy=0
        elif direc == 270:
            dx=0
            dy=-1
    print(abs(x)+abs(y))


@timer
def part_2():
    I = read_file('day12')
    x = 0
    y = 0
    wx = 10
    wy = 1
    direc = 0
    for i in I:
        action = i[0]
        val = int(i[1:])
        if action == 'F':
            x+=val*wx
            y+=val*wy
        elif action == 'N':
            wy += val
        elif action == 'S':
            wy -= val
        elif action == 'W':
            wx -= val
        elif action == 'E':
            wx += val
        elif action == 'L':
            direc = val
        elif action == 'R':
            direc = 360 - val

        while direc != 0:
            wx_new = -wy
            wy_new = wx
            wx = wx_new
            wy = wy_new
            direc -= 90
    print(abs(x)+abs(y))
    pass


part_1()
part_2()
