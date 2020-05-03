#collections module
from collections import Counter, defaultdict, namedtuple, ChainMap, deque, OrderedDict, UserDict, UserList, UserString

point = namedtuple('point', 'x, y')

point.x = 0
point.y = 1

print(f'({point.x}, {point.y})')

point1 = point._make([2, 3])
point2 = point._make([4, 5])
print(point1)
print(point2)

a = ['a', 'e', 'i', 'o', 'u']

d = deque(a)
print(d)
d.append('z')  #appends value in the right side
print(d)
d.appendleft('y') #appends value in the left side
print(d)
d.pop() #pops value from the right side
print(d)
d.popleft() #pops value from the left side
print(d)

d1 = {1:'a', 2:'b'}
d2 = {3:'c', 4:'d'}

c = ChainMap(d1, d2)

print(c)

string = "stayhomestaysafe"
print(Counter(string))

d_int = defaultdict(int)
d_int['a'] = 1
d_int['b'] = 2
print(d_int['c'])

