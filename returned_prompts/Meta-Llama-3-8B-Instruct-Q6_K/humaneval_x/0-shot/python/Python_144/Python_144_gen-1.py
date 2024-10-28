```
def simplify(x, n):
    # convert the fractions to integers
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    # convert the fractions to a common denominator
    common_den = x_den * n_den
    
    # convert both fractions to the common denominator
    x_num *= x_den
    n_num *= n_den
    
    # calculate the product of the fractions
    product_num = x_num * n_num
    product_den = common_den
    
    # check if the product is a whole number
    if product_den % product_num == 0:
        return True
    else:
        return False
```


This function first converts the input fractions to integers, then it calculates the common denominator for the two fractions. It then converts both fractions to this common denominator and calculates the product of the two fractions. Finally, it checks if the product is a whole number by checking if the denominator is a multiple of the numerator. If it is, the function returns True, otherwise it returns False.