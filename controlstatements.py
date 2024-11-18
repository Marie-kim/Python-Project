temperature = int(input("Enter temperature"))

if temperature > 25:
    print("it is too hot")
else:
    print("it is too cold")

# A python program that checks three numbers and returns the smallest
num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))
num3 = int(input("Enter first number: "))

if num1 < num2 and num1 < num3:
    print(num1,"is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2,"is the smallest number")
else:
    print(num3,"is the smallest number")


if num1 > num2 and num1 > num3:
    print(num1,"is the biggest number")
elif num2 > num1 and num2 > num3:
    print(num2,"is the biggest number")
else:
    print(num3,"is the biggest number")

    