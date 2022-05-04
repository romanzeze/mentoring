def kluci(r):
    keys = sorted(r, key=r.get, reverse=True)[:3]
    print(keys)
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

kluci(my_dict)