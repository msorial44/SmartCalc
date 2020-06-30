from collections import deque
import math

numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
var_dict = {}
math_check = 0
covert_in_stack = deque()
number = 0
letter = 0
convert_post_stack = deque()
converted_var_str = ''
post_eq = []
temp_list = []
math_counter = 0
final_eq = ''


def convert_post(x_str):
    x_list = x_str.split(' ')
    for x in x_list:
        if '(' in x and len(x) > 1:
            bee_boop = list(x)
            big_index = x_list.index(x)
            del x_list[big_index]
            xbex = bee_boop[0]
            del bee_boop[0]
            boopy = "".join(bee_boop)
            x_list.insert(big_index, boopy)
            x_list.insert(big_index, xbex)

        elif ')' in x and len(x) > 1:
            bee_boop = list(x)
            big_index = x_list.index(x)
            del x_list[big_index]
            xbex = bee_boop[-1]
            del bee_boop[-1]
            boopy = "".join(bee_boop)
            x_list.insert(big_index, xbex)
            x_list.insert(big_index, boopy)

    for x in x_list:
        if x == '*' or x == '/':
            try:
                xy = convert_post_stack.pop()
                convert_post_stack.append(xy)
            except IndexError:
                convert_post_stack.append(x)
            else:
                if xy == '(':
                    convert_post_stack.append(x)
                elif xy == '+' or xy == '-':
                    convert_post_stack.append(x)
                else:
                    temp_list = []
                    for xs in convert_post_stack:
                        temp_list.append(xs)
                    for xs in temp_list:
                        if len(convert_post_stack) == 0:
                            convert_post_stack.append(x)
                        elif xs == '(':
                            convert_post_stack.append(x)
                        elif xs == '+' or xs == '-':
                            convert_post_stack.append(x)
                        else:
                            xp = convert_post_stack.pop()
                            post_eq.append(xp)
                            convert_post_stack.append(x)
        elif x == '+' or x == '-':
            try:
                xy = convert_post_stack.pop()
                convert_post_stack.append(xy)
            except IndexError:
                convert_post_stack.append(x)
            else:
                if xy == '(':
                    convert_post_stack.append(x)
                else:
                    temp_list = []
                    for xs in convert_post_stack:
                        temp_list.append(xs)
                    for xs in temp_list:
                        if len(convert_post_stack) == 0:
                            convert_post_stack.append(x)
                        elif xs == '(':
                            convert_post_stack.append(x)
                        else:
                            xp = convert_post_stack.pop()
                            post_eq.append(xp)
                            convert_post_stack.append(x)
        elif '^' in x:
            convert_post_stack.append(x)
        elif x == '(':
            convert_post_stack.append(x)
        elif x == ')':
            temp_list.clear()
            for xps in convert_post_stack:
                temp_list.append(xps)
            for xs in temp_list:
                if xs == '(':
                    convert_post_stack.pop()
                    break
                else:
                    xy = convert_post_stack.pop()
                    post_eq.append(xy)
        else:
            post_eq.append(x)

    temp_list = []
    for x in convert_post_stack:
        temp_list.append(x)
    for x in temp_list:
        xy = convert_post_stack.pop()
        post_eq.append(xy)


def non_math_checks(x_str):
    if x_str == '/help':
        print('This is a smart calculator with all basic operations and variables included')
        return 1
    elif x_str.startswith('/'):
        print('Unknown Command')
        return 1
    elif x_str == ' ':
        return 1
    elif not x_str and not x_str.strip():
        return 1


def check_for_assign(x_str):
    if any(y in x_str for y in letters) and '=' in x_str:
        y_list = x_str.split('=')
        if len(y_list) > 2:
            print('Invalid Assignment')
            return 1
        if len(y_list) == 2:
            if any(y in y_list[0] for y in numbs):
                print('Invalid Identifier')
                return 1
            elif any(y in y_list[1] for y in letters) and any(y in y_list[1] for y in numbs):
                print('Invalid Assignment')
                return 1
            elif any(y in y_list[1] for y in letters):
                if y_list[1].strip(' ') in var_dict:
                    bshh = var_dict[y_list[1].strip(' ')]
                    del y_list[1]
                    y_list.append(bshh)
                    var_dict[y_list[0].strip(' ')] = y_list[1].strip(' ')
                    return 1
                else:
                    print('Unknown Variable')
                    return 1
            else:
                var_dict[y_list[0].strip(' ')] = y_list[1].strip(' ')
                return 1
    if any(y in x_str for y in letters) and '=' not in x_str:
        y_list = x_str.split()
        if len(y_list) == 1:
            if x_str in var_dict:
                print(var_dict[x_str])
                return 1
            else:
                print('Unknown Variable')

    elif any(y in x_str for y in numbs) and not any(y in x_str for y in letters):
        y_list = x_str.split()
        if len(y_list) == 1:
            print(x_str)
            return 1


def mathsman(x_str):
    covert_in_stack.clear()
    math_counter = 0
    x_list = x_str.split(' ')
    mathi_check = len(x_list)
    while math_counter < mathi_check:
        temp_list = []
        for x in x_list:
            temp_list.append(x)
        for x in temp_list:
            number = 0
            letter = 0
            for y in numbs:
                if y in x:
                    number = 1
                    break
            if number == 1:
                covert_in_stack.append(x)
                del x_list[x_list.index(x)]
            else:
                for y in letters:
                    if y in x:
                        letter = 1
                        break
            if letter == 1:
                if x in var_dict:
                    covert_in_stack.append(var_dict[x])
                    del x_list[x_list.index(x)]
                else:
                    print('Unknown Variable')
                    return
            elif '+' in x:
                del x_list[x_list.index(x)]
                x2 = covert_in_stack.pop()
                x1 = covert_in_stack.pop()
                x3 = int(x1) + int(x2)
                covert_in_stack.append(x3)
            elif '-' in x:
                if (len(x) % 2) == 0:
                    del x_list[x_list.index(x)]
                    x1 = covert_in_stack.pop()
                    x2 = covert_in_stack.pop()
                    x3 = int(x1) + int(x2)
                    covert_in_stack.append(x3)
                else:
                    del x_list[x_list.index(x)]
                    x2 = covert_in_stack.pop()
                    x1 = covert_in_stack.pop()
                    x3 = int(x1) - int(x2)
                    covert_in_stack.append(x3)
            elif '*' in x:
                if len(x) == 1:
                    del x_list[x_list.index(x)]
                    x1 = covert_in_stack.pop()
                    x2 = covert_in_stack.pop()
                    x3 = int(x1) * int(x2)
                    covert_in_stack.append(x3)
                else:
                    print('Invalid Expression')
                    return
            elif '/' in x:
                if len(x) == 1:
                    del x_list[x_list.index(x)]
                    x2 = covert_in_stack.pop()
                    x1 = covert_in_stack.pop()
                    x3 = int(x1) / int(x2)
                    covert_in_stack.append(x3)
                else:
                    print('Invalid Expression')
                    return
            elif '^' in x:
                ex_valid_check = list(x)
                if ex_valid_check.count('^') > 1:
                    print('Invalid Expression')
                    return
                else:
                    ex_list = x.split('^')
                    covert_in_stack.append(math.pow(ex_list[0], ex_list[1]))
                    del x_list[x_list.index(x)]
            math_counter += 1
    print(covert_in_stack[0])
    del covert_in_stack[0]


def reset():
    post_eq.clear()
    post_eq1 = ''
    convert_post_stack.clear()
    covert_in_stack.clear()
    temp_list.clear()


def unbalance_parantheses(x_str):
    x_list = x_str.split(' ')
    left_counter = 0
    right_counter = 0
    for x in x_list:
        if '(' in x and len(x) > 1:
            bee_boop = list(x)
            big_index = x_list.index(x)
            del x_list[big_index]
            xbex = bee_boop[0]
            del bee_boop[0]
            boopy = "".join(bee_boop)
            x_list.insert(big_index, boopy)
            x_list.insert(big_index, xbex)
        elif ')' in x and len(x) > 1:
            bee_boop = list(x)
            big_index = x_list.index(x)
            del x_list[big_index]
            xbex = bee_boop[-1]
            del bee_boop[-1]
            boopy = "".join(bee_boop)
            x_list.insert(big_index, xbex)
            x_list.insert(big_index, boopy)
    for x in x_list:
        if x == '(':
            left_counter += 1
        if x == ')':
            right_counter += 1
    if right_counter != left_counter:
        print('Invalid Expression')
        return 1

while True:
    xxxx = 0
    reset()
    math_check = 0
    var_check = 0
    og_str = input()
    if og_str == '/exit':
        print('Bye!')
        break
    if non_math_checks(og_str) == 1:
        math_check = 1
        var_check = 1

    if var_check == 0:
        if check_for_assign(og_str) == 1:
            math_check = 1
        else:
            if unbalance_parantheses(og_str) == 1:
                math_check = 1
            else:
                convert_post(og_str)
    post_eq1 = ' '.join(post_eq)
    if math_check == 0:
        mathsman(post_eq1)
