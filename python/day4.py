from common import read_file, timer
import re


@timer
def part_1():
    input_data = read_file('day4')
    input_data.append('')
    count = 0
    s = set()
    for l in input_data:
        if l == '':
            s.discard('cid')
            if len(s) == 7: count += 1
            s = set()
        else:
            s = s | set(map(lambda x: x.split(':')[0], l.split(' ')))

    print(count)


@timer
def part_2():
    input_data = read_file('day4')
    input_data.append('')
    count = 0
    s = set()
    for l in input_data:
        if l == '':
            count += validate(s)

            s = set()
        else:
            s = s | set(l.split(' '))

    print(count)


def validate(s):
            """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
            """
            byr = [x for x in s if x.startswith('byr')]
            iyr = [x for x in s if x.startswith('iyr')]
            eyr = [x for x in s if x.startswith('eyr')]
            hgt = [x for x in s if x.startswith('hgt')]
            hcl = [x for x in s if x.startswith('hcl')]
            ecl = [x for x in s if x.startswith('ecl')]
            pid = [x for x in s if x.startswith('pid')]
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                byr_d = int(byr[0][4:])
                if byr_d < 1920 or byr_d > 2002: return 0

                iyr_d = int(iyr[0][4:])
                if iyr_d < 2010 or iyr_d > 2020: return 0

                eyr_d = int(eyr[0][4:])
                if eyr_d < 2020 or eyr_d > 2030: return 0

                hgt_d = hgt[0][4:]
                if not (hgt_d.endswith('cm') or hgt_d.endswith('in')): return 0
                hgt_d_i = int(hgt_d[:-2])
                hgt_d_u = hgt_d[-2:]
                if hgt_d_u == 'cm' and (hgt_d_i < 150 or hgt_d_i > 193): return 0
                if hgt_d_u == 'in' and (hgt_d_i < 59 or hgt_d_i > 76): return 0

                hcl_d = hcl[0][4:]
                if not re.search(r'^#[0-9a-f]{6}$', hcl_d): return 0

                ecl_d = ecl[0][4:]
                if ecl_d not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return 0

                pid_d = pid[0][4:]
                if not re.search(r'^\d{9}$', pid_d): return 0
    
                return 1
            return 0


part_1()
part_2()
