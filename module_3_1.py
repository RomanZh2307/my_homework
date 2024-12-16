# calls = 0
# def count_calls():
#     global calls
#     calls += 1
#
# def string_info(string):
#     line = str(string)
#     result = (len(line), line.upper(), line.lower())
#     count_calls()
#     return result
#
# def is_contains(string, list_to_search):
#     string = str(string).lower()
#     list_to_search = list(list_to_search)
#     count_calls()
#     for i in range(len(list_to_search)):
#         if str(list_to_search[i]).lower() == string:
#             result = True
#             break
#         else:
#             result = False
#             continue
#     return result
#
# print(string_info('Capybara'))
# print(string_info('Armageddon'))
# print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
# print(is_contains('cycle', ['recycling', 'cyclic']))
#
# print(calls)

calls = 0  # Эту переменную лучше всего переносить к остальным глобальным переменным(ОТМЕТИЛ НИЖЕ ГДЕ ИМЕННО)


def count_calls():


global calls

calls += 1


def string_info(string):


line = str(string)  # Нам не нужно строку превращать в строку

result = (len(line), line.upper(), line.lower())  # Можно просто вернуть весь кортеж без result =

count_calls()

return result  # (len(line), line.upper(), line.lower()) ВОТ ТАК


def is_contains(string, list_to_search):


string = str(string).lower()  # Нам не нужно строку превращать в строку .lower() остаётся,а str нам тут не нужно

list_to_search = list(list_to_search)  # Нам не нужно список превращать в список

count_calls()

for i in range(len(list_to_search)):  # Цикл фор позволяет сразу перебирать элементы, нам не нужны индексы

if str(list_to_search[i]).lower() == string:  # Нам не нужно строчный элемент превращать в строку

result = True  # ПУНКТ 1

break  # ПУНКТ 2

# Мы можем Пункт 1 и Пункт 2 объединить в просто return True

else:  # Тогда мы сможем отказаться от блока else

result = False  # это уберём

continue  # это уберём

return result  # А тут просто вернём False, т.к. если получим True Программа сюда не доберётся.

# Эту переменную лучше всего переносить к остальным глобальным переменным (ВОТ СЮДА)

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))

print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
