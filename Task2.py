#номер вариант для 2 задания: 3

import re

test1 = "Студент Вася вспомнил, что на своей лекции Балакшин П.В. упоминал про старшекурсников, которые будут ему помогать: Анищенко А.А. и Машина Е.А."
test2 = "Чмурова М.В. очень хотела сдать третью лабу поскорее"
test3 = "Станция метро 'Горьковская' названа в честь писателя Горького М., настоящие инициалы которого - Пешков А.М."
test4 = "Сидоров А.И. и Иванов И.Т. учились в одном классе"
test5 = "Если Чмурова пересдаст ЕГЭ в этом году, то получит бесплатную подписку на Яндекс Плюс на весь следующий год"

testall = [test1, test2, test3, test4, test5]

for i in range(5):
    reg_new = list()
    reg = re.findall(r'[А-Я]{1}[а-я]*\s[А-Я]\.[А-Я]\.', testall[i])
    print("Результат для теста", i+1)
    if len(reg) == 0:
        print("Фамилий не найдено")
    else:
        for j in range(len(reg)):
            reg_new.append(''.join(re.findall(r'[А-Я][а-я]+', reg[j])))
            reg_new.sort()
        print(*reg_new)



