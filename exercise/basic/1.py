# Calculate Multiplication and sum of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def multiplication(num1, num2):
    return num1 * num2

def sum(num1, num2):
    return num1 + num2

print(f"{a} x {b} = {multiplication(a, b)}")
print("%d + %d = %d" % (a, b, sum(a, b)))