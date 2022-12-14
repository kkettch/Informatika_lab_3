#номер вариант для 2 задания: 3

#Дан текст. Требуется найти в тексте все фамилии, отсортировав их по алфавиту.
#Фамилией для простоты будем считать слово с заглавной буквой, после которого идут инициалы

import re

test1 = "Студент Вася вспомнил, что на своей лекции Балакшин П.В. упоминал про старшекурсников, которые будут ему помогать: Анищенко А.А. и Машина Е.А."
test2 = "Чмурова М.В. очень хотела сдать третью лабу поскорее"
test3 = "Станция метро 'Горьковская' названа в честь писателя Горького М., настоящие инициалы которого - Пешков А.М."
test4 = "Сидоров А.И. и Иванов И.Т. учились в одном классе"
test5 = "Если Чмурова пересдаст ЕГЭ в этом году, то получит бесплатную подписку на Яндекс Плюс на весь следующий год"

testall = [test1, test2, test3, test4, test5]

for i in range(5):
    reg_new = list()
    #создаем лист, чтобы в будущем записывать в него фамилии без инициалов
    reg = re.findall(r'[А-Я]{1}[а-я]*\s[А-Я]\.[А-Я]\.', testall[i])
    #находим фамилии с инициалами в тестах
    print("Результат для теста", i+1)
    if len(reg) == 0:
        print("Фамилий не найдено")
        #если в лист не добавился ни один элемент, значит в тексте нет фамилий с инициалами
    else:
        for j in range(len(reg)):
            reg_new.append(''.join(re.findall(r'[А-Я][а-я]+', reg[j])))
            #добавляем в массим фамилии без инициалов
            reg_new.sort()
            #сортируем массив с фамилиями в алфавитном порядке
        print(*reg_new)
        #при выводе фамилий пишем звездчку перед азванием листа, чтобы вывести фамилии без кавычек



