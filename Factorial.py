num = int(input("Enter a number: "))
fact = 1
if num < 0:
    print("Invalid")
elif num == 0:
    print("1")
else:
    for i in range(1, num + 1):
        fact = fact * i
print(f"Factorial of {num} is:", fact)