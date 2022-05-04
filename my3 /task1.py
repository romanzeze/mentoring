def sum_range(start, end):
    if start > end:
        start, end = end, start
    s = 0
    for i in range(start, end + 1):
        s += i
    print(s)


a=int(input("a="))
b=int(input("b="))
sum_range(a,b)