number = int(input("Enter a number: "))
result = []
for i in range(1, 20):
    for j in range(2, 20):
        if i < j and number % (i + j) == 0:
            result.append(i)
            result.append(j)
            continue
        if i < j and i + j == number:
            result.append(i)
            result.append(j)
            break
print(f"{number} - {''.join(str(el) for el in result)}")
