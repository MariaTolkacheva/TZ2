# opening the file
f = open('numbers.txt', 'r')
# a list with all our numbers
str_num = []
for x in f:
    str_num += x.split()


def num_min(list_num):
    try:
        print(min(int(x) for x in list_num))
    except ValueError:
        pass


def division(a, b):
    return a / b


def num_sum(a):
    s = 0
    for i in a:
        try:
            s += int(i)
        except ValueError:
            print('no', i)


num_sum(str_num)
num_min(str_num)
