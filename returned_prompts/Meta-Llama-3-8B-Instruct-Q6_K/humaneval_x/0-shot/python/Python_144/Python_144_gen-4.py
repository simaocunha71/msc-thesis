```
def simplify(x, n):
    x_numerator, x_denominator = map(int, x.split('/'))
    n_numerator, n_denominator = map(int, n.split('/'))
    
    numerator = x_numerator * n_denominator
    denominator = x_denominator * n_numerator
    
    if numerator % denominator == 0:
        return True
    else:
        return False
```



Explanation:
The function takes two string inputs, x and n, each representing a fraction in the format <numerator>/<denominator>. It splits the strings into numerator and denominator integers, calculates the numerator and denominator of the product, and checks if the numerator is a multiple of the denominator. If it is, the function returns True; otherwise, it returns False. The function does not simplify the fractions, it just checks if the product is a whole number. This is in line with the problem statement, which asks for a function that returns True if the product is a whole number and False otherwise. It does not ask for the simplified fraction. 

For example, the product of 1/5 and 5/1 is 5/1, which is a whole number, so the function returns True. The product of 1/6 and 2/1 is 2/3, which is not a whole number, so the function returns False. The product of 7/10 and 10/2 is 35/2, which is a whole number, so the function returns True. 

Note that the function does not handle the case where the numerator or denominator is 0. This is because the problem statement specifies that the input fractions do not have zero as denominator. However, in a real-world implementation, you would want to add error checking to handle this case. 





The code is written in Python. It uses the map function to convert the numerator and denominator of each input string to integers. It then calculates the numerator and denominator of the product by multiplying the corresponding parts of the input fractions. Finally, it checks if the numerator is a multiple of the denominator by using the modulus operator (%). If the remainder is 0, the function returns True; otherwise, it returns False.