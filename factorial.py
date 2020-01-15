number = int(input("number : " ))

factorial = 1

if number < 0:
    print("factorial of negative numbers is not calculated")
elif number == 0:
    print("result = 1 ")
else:
    for i in range(1,number + 1):
        factorial = factorial * i 
    print("result = ", factorial)