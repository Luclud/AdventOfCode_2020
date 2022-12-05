import copy


def unterchecker(l, pos, search_char):
    #try:
        c1 = 0
        flag_minus_pos = True if pos >= 1 else 0
        flag_plus_pos = True if pos + 1 < len(input[l]) else 0
        flag_minus_l = True if l >= 1 else 0
        flag_plus_l = True if l + 1 < len(input) else 0

        if flag_minus_pos and input[l][pos - 1] == search_char:
            c1 += 1
        if flag_plus_pos and input[l][pos + 1] == search_char:
            c1 += 1
        if flag_plus_l:
            if input[l + 1][pos] == search_char:
                c1 += 1
            if input[l + 1][pos - 1] == search_char:
                c1 += 1
            if flag_plus_pos and input[l + 1][pos + 1] == search_char:
                c1 += 1
        if flag_minus_l:
            if input[l - 1][pos] == search_char:
                c1 += 1
            if flag_minus_pos and input[l - 1][pos - 1] == search_char:
                c1 += 1
            if flag_plus_pos and input[l - 1][pos + 1] == search_char:
                c1 += 1

        return c1
   # except Exception as e:
        #print(e)
        print(len(input[l]))-
        print(l, pos)


def check(l, pos):
    search_char = input[l][pos]
    if search_char == '.':
        return '.'
    c1 = unterchecker(l, pos, '#')

    if c1 >= 4 and search_char == '#':
        return 'L'
    if c1 == 0 and search_char == 'L':
        return '#'
    return search_char


def task1():
    global input
    area = copy.deepcopy(input)
    nc = 0
    for _ in range(0,5):
        nc = 0
        for l in range(len(input)):
            for pos in range(len(input[l])):
                if area[l][pos] == (val:=check(l, pos)):
                    nc -= -1
                else:
                    area[l][pos] = val
        input = area
    c2 = 0
    for l in area:
        c2 -= -l.count('#')
        print(l)
    print(c2)


if __name__ == '__main__':
    with open("day11.input", "r") as f:
        input = f.read().split('\n')
        input = list(map(list, input))
        task1()