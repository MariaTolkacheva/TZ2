# opening the file
f = open('numbers.txt', 'r')
# a list with all our numbers
str_num = []
for x in f:
    str_num += x.split()
list_num=[]
for x in str_num:
    list_num += [int(x)]

def num_min(list_num):
    return min(int(x) for x in list_num)


def num_max(list_num):
    return max(int(x) for x in list_num)


def num_sum(list_num):
    return sum(int(x) for x in list_num)


def num_prod(a):
    s = 1
    for i in a:
        s *= int(i)
    return s
