# while 1 > 0:  # либо True
#     number = int(input("Enter a number: "))
#     if number % 2 == 0:
#         print("Число четное")
#         continue  # пропускаетна следующий цикл
#     else:
#         print("Число нечетное")
# print("Я за циклом")
#
# а = 5


# my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# num = 0
# while num < len(my_list):
#     if my_list[num] > 0:
#         print(my_list[num])
#         num += 1
#         continue
#     if my_list[num] == 0:
#         num += 1
#         continue
#     else:
#         break

# for i in 1, 2, 3, 4: # последовательностьпо кол-ву символов
#     print(i)
#
# for i in "hello":
#     print(i)

# list_ = ["one", "two", "three"]
# for i in list_:
#     if i == "three":
#         list_.remove(i)
#
# print(list_)

# list_ = ["one", "two", "three"]
# for i in range(5): # данная функция возвращает последовательность чиселот 0 до того числа в скобках # 0, 1, 2, 3, 4
# # вместо числа можно range(len(list_[i]))
#     print(i)
#
# print(list_)

# функция range() принимает три параметра start, stop, step обязательный стоп, (1, 11) начало и стоп, step это шаг

# for i in range(1, 11): # i - 1 и т.д
#     for j in range(1, 11): # j - 1 и т.д.
#         print(f"{i} x {j} = {i * j}")
#
# dict_ = {"a": 1, "b": 2, "c": 3}
# for i in dict_:
#     print(i, dict_[i])

dict_ = {"a": 1, "b": 2, "c": 3}
for i, k in dict_.items():
    print(i, k)