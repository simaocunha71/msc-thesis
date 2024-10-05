
def simplify(x, n):
    x_num, x_den = [int(i) for i in x.split('/')]
    n_num, n_den = [int(i) for i in n.split('/')]
    if x_den == n_den:
        return x_num * n_num == x_den
    else:
        x_num = x_num * n_den
        x_den = x_den * n_den
        n_num = n_num * x_den
        n_den = n_den * x_den
        if x_num % x_den == 0 and n_num % n_den == 0:
            return True
        return False

# simplify("1/5", "5/1") # True
# simplify("1/6", "2/1") # False
# simplify("7/10", "10/2") # False



# simplify("1/6", "7/2") # True
# simplify("1/5", "6/2") # False
# simplify("1/4", "4/2") # True
# simplify("1/3", "3/2") # False
# simplify("1/2", "2/2") # True
# simplify("1/2", "3/2") # False
# simplify("3/4", "4/2") # False
# simplify("7/8", "8/2") # False
# simplify("3/4", "8/4") # True
# simplify("1/3", "8/3") # False
# simplify("7/8", "12/8") # True
# simplify("1/3", "24/9") # True
# simplify("7/8", "36/24") # True
# simplify("1/3", "27/9") # False
# simplify("7/8", "54/24") # False
# simplify("1/3", "81/9") # True
# simplify("7/8", "72/24") # False
# simplify("