sum_squares = lambda lst: sum(i ** 2 if i % 3 == 0 else (i ** 3 if i % 4 == 0 and i % 3 else i) for i in lst)


# Testing:
print(sum_squares([1, 2, 3]))  # should print 6
print(sum_squares([]))  # should print 0
print(sum_squares([-1, -5, 2, -1, -5]))  # should print -126

































```  
```