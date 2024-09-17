```
def find_Index(n):
    i = 1
    triangular_nums = []
    while True:
        triangular_num = sum(range(1, i+1))
        triangular_nums.append(triangular_num)
        if str(triangular_num).__len__() == n:
            return triangular_nums.index(triangular_num)
        i += 1
```    
The problem is asking to find the smallest triangular number that has n digits. The function first initializes a variable i to 1 and an empty list triangular_nums. It then enters a loop where it calculates each triangular number using the formula sum(range(1, i+1)) and appends it to the list. The loop continues until the triangular number has n digits. Once the triangular number has n digits, the function returns the index of this number in the list, which is the smallest triangular number with n digits. The unit test `assert find_Index(2) == 4` means that the smallest triangular number with 2 digits is the 4th triangular number, which is 6.