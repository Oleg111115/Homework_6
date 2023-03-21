import itertools

list = [1, 2, 3]
mixing = itertools.permutations(list)
for i in mixing:
    print(i)
