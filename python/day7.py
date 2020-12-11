from common import read_file, timer
import re

@timer
def part_1():
    I = read_file('day7')
    fringe = ['shiny gold']
    total = set()

    while fringe:
        fringe = [' '.join(x.split(' ')[:2])
                for x in I for f in fringe if f in ' '.join(x.split(' ')[4:])]
        total.update(fringe)

    print(len(total))


@timer
def part_2():
    I = read_file('day7')
    fringe = [('shiny gold', 1)]
    total_bags = []

    while fringe:
        head = fringe[0]
        contents = [' '.join(x.split(' ')[4:]) for x in I if x.startswith(head[0])][0]
        if contents.endswith('no other bags.'):
            total_bags.append(head)
            fringe = fringe[1:]
        else:
            next_bags = [(' '.join(x.split(' ')[1:]), int(' '.join(x.split(' ')[0])) * head[1])
                  for x in re.sub(r' bags?\.?', '', contents).split(', ')]
            total_bags.append(head)
            fringe = fringe[1:]
            fringe += next_bags

    print(sum(int(x) for _, x in total_bags) - 1)


part_1()
part_2()
