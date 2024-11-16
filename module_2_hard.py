number = int(input("Enter a number: "))
pass_num = []
for i in range(1,20):
     for j in range(2,20):
          if i < j and number % (i + j) == 0:
               pass_num.append(i)
               pass_num.append(j)
               continue
          if i < j and i + j == number:
               pass_num.append(i)
               pass_num.append(j)
               break
print(pass_num)
