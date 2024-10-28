```
def simplify(x, n):
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    # Calculate the common denominator
    common_den = max(x_den, n_den)
    
    # Calculate the new numerator for x and n
    new_x_num = x_num * (common_den // x_den)
    new_n_num = n_num * (common_den // n_den)
    
    # Check if the result is a whole number
    if new_x_num % common_den == 0 and new_n_num % common_den == 0:
        return True
    else:
        return False
```


This function splits the input strings into numerators and denominators, calculates the common denominator, and then checks if the result is a whole number by checking if the numerator is a multiple of the denominator. If both conditions are met, it returns True, otherwise False.