list = input("Введите слова через пробел: ")
words = [word for word in list.split()]
words.sort()
print(words)