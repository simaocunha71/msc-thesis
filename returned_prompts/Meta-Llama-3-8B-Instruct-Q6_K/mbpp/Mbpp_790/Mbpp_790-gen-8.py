```
def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True
```    
The unit test `assert even_position([3,2,1]) == False` helps to understand the problem better. It means that for the given list [3,2,1], the function should return False because the even position (1-indexed) has an odd number.

The function `even_position` takes a list `lst` as an argument and checks every even index in the list. It uses a for loop to iterate over the list with a step of 2, which means it checks every even index. If it finds an index where the number is not even (i.e., the remainder when divided by 2 is not 0), it immediately returns False. If it checks all the even indices and finds no odd numbers, it returns True. 