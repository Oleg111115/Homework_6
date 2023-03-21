list = [1, 2, 3]
combinations_list = []
combinations_list.append([list[0], list[1], list[2]])
combinations_list.append([list[0], list[2], list[1]])
combinations_list.append([list[1], list[2], list[0]])
combinations_list.append([list[1], list[0], list[2]])
combinations_list.append([list[2], list[0], list[1]])
combinations_list.append([list[2], list[1], list[0]])
print(combinations_list)