# Print the sum of current and prev number:

a = int(input("Enter first number: "))

def sum(num1, num2):
    return num1 + num2
prev = 0
curr = 0
for i in range(a):
    print(f"{prev} + {curr} = {sum(prev, curr)}")
    prev = curr
    curr = curr + 1
