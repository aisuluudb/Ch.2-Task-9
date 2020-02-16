numb = 10
factorial = 1
if numb > 0:
    print()
elif numb == 0:
    print(1)
else:
    for i in range (1, numb + 1):
        factorial = factorial * i
print(factorial)