word = input()
number = 1
word2 = ''
for index in word:
    word2 += index * number
    number += 1
print(word2)
