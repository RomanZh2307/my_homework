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


my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
while num < len(my_list):
    if my_list[num] > 0:
        print(my_list[num])
        num += 1
        continue
    if my_list[num] == 0:
        num += 1
        continue
    else:
        break









