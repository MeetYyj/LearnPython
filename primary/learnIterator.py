from collections import Iterable
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
  print(key)

for ch in 'ABC':
  print(ch)

isinstance('abc', Iterable)
isinstance([1, 2, 3], Iterable)
isinstance(123, Iterable)

for key, value in enumerate(['A', 'B', 'C']):
  print(key, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
  print(x, y)
