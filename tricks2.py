import itertools
import operator

counter = itertools.count() #counts from zero to infinity

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

for num in counter:
	infinite loop
	print(num)

data = [100, 200, 300, 400]

daily_data = list(zip(itertools.count(), data))	#normal zip function ---- till the smallest iterables is exhausted

print(daily_data)

data = [100, 200, 300, 400]

daily_data = list(itertools.zip_longest(range(10), data))	#normal zip_longest function ---- till the largest iterables is exhausted default None

print(daily_data)

counter = itertools.cycle([1, 2, 3])

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

Simulating a switch using the cycle function 

counter = itertools.cycle(('on', 'off'))

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter = itertools.repeat(2, times=8)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

Squaring numbers using the repeat function

squares = map(pow, range(10), itertools.repeat(2))

print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))

squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2), (3, 2)]) # takes list of tuples as argument

print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Ayush', 'Atharva']

results = itertools.combinations(letters, 2)

for result in results:
	print(result)

results = itertools.permutations(letters, 4)

for result in results:
	print(result)

results = itertools.product(numbers, repeat=4)

for result in results:
	print(result)

results = itertools.combinations_with_replacement(numbers, 4)

for result in results:
	print(result)

combined = itertools.chain(letters, numbers, names)

for item in combined:
	print(item)

result = itertools.islice(range(10), 1, 10, 2)

for item in result:
	print(item)

with open('test.txt', 'r') as f:
	header = itertools.islice(f, 3)

	for line in header:
		print(line, end='')

selectors = [True, True, False, True]

result = itertools.compress(letters, selectors)

for item in result:
	print(item)

def lt_2(n):

	if n<2:
		return True
	return False

result = filter(lt_2, numbers)  # returns values where condition is true

for item in result:
	print(item)

result = itertools.filterfalse(lt_2, numbers)  # returns values where condition is false

for item in result:
	print(item)

numbers = [0, 1, 2, 3, 2, 1, 0]

result = itertools.dropwhile(lt_2, numbers)

for item in result:
	print(item)

result = itertools.takewhile(lt_2, numbers)

for item in result:
	print(item)

result = itertools.accumulate(numbers) # buy default adds

for item in result:
	print(item)

numbers = [1, 2, 3, 4, 5]

result = itertools.accumulate(numbers, operator.mul)

for item in result:
	print(item)

def get_state(person):
	return person['state']

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

person_group = itertools.groupby(people, get_state)

for key, group in person_group:
	print(key)
	for person in group:
		print(person)
	print()

for key, group in person_group:
	print(key, len(list(group))

copy1, copy2 = itertools.tee(person_group)