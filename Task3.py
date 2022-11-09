#Вариант для третьего задания: 2

import re

test1 = "20 + 22 = 42"
test2 = "20 30 500 текст текст текст"
test3 = "сообщение без цифр"
test4 = "10 100 1000 - любые цифры принимает для кодировки!"
test5 = "Мне 18 лет"

testall = [test1, test2, test3, test4, test5]

for i in range(5):
    reg = re.findall(r'\d+', testall[i])
    if len(reg) == 0:
        print("В сообщении нет символов, которые можно закодировать")
    else:
        for j in range(len(reg)):
            new = str(4 * int(reg[j])**2 - 7)
            testall[i] = re.sub(re.escape(reg[j]), re.escape(new), testall[i])
        print(testall[i])

