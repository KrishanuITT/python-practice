#  Given list and n find no's divisible by n

def divisible_by_n(lst, n):
    return [i for i in lst if i % n == 0]


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
print(divisible_by_n(lst, n))