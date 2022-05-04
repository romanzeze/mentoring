def List(data, f):
   a = []
   a.append(data)
   for a in data:
      f.write(a)


def tuple(data, f):
   d = tuple(map(str, data))
   for d in data:
      f.write(d)


f = open('fail3.pages', 'r+')
data = f.readline()
List(data, f)
tuple(data, f)
f.close()
