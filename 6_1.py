list = input("Введите слова через пробел: ")
words = [word for word in list.split()]
words.sort()
print(words)


#Пример:

#Введите слова через пробел: яблоко груша апельсин банан
#['апельсин', 'банан', 'груша', 'яблоко']