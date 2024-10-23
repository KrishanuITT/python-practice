# Check if first and last no of list are same

def check_list(lst):
    if lst[0] == lst[-1]:
        return True
    return False


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(check_list(lst))


lstT = [1, 1]
print(check_list(lstT))