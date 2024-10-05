```
def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        return x == y + z or x == z + y or y == x + z or y == z + x or z == x + y
    else:
        return False
```    
The function any_int checks if the input numbers are integers and if the sum of any two numbers is equal to the third number. If the input numbers are integers and the sum condition is met, the function returns True. Otherwise, it returns False. The function uses the isinstance() function to check if the input numbers are integers, and the or operator to check if the sum condition is met. The sum condition is checked for all possible combinations of the input numbers. If the sum condition is met for any combination, the function returns True. If the sum condition is not met for any combination, the function returns False.