def odd_num_sum(n):
    return sum([x**4 for x in range(1, n+1, 2)])

#Alternative
def odd_num_sum(n):
    return sum([x**4 for x in range(1, n+1, 2)])
    
#Alternative
def odd_num_sum(n):
    return sum(x**4 for x in range(1, n+1, 2))