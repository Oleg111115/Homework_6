import itertools

list = [1, 2, 3]
mixing = itertools.permutations(list)
for i in mixing:
    print(i)

#(1, 2, 3)
#(1, 3, 2)
#(2, 1, 3)
#(2, 3, 1)
#(3, 1, 2)
#(3, 2, 1)