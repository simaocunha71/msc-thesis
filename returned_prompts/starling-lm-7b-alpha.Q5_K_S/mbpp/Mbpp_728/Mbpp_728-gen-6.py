sum_list = lambda x,y : [i+j for i,j in zip(x,y)]

# Alternatively,
sum_list = lambda x,y : [sum(a) for a in zip(x,y)]


# Python program to add corresponding
# elements of two lists
def sum_list(x, y):
    z = [] 
    for i in range(len(x)):
        z.append(x[i] + y[i])
    return z
    
def sum_list(X, Y):
    return [X[i]+Y[i] for i in range(len(X))]

def sum_list(X,Y):
    return [x+y for x,y in zip(X,Y)]

"""
The above Python program defines a function sum_list() which takes two lists as input and returns the sum of corresponding elements of the two lists. It returns a list containing the sum.

The function sum_list() uses list comprehension to calculate the sum of the elements of the two lists. It iterates over the indices of the lists and adds the elements at corresponding indices to obtain the resultant sum.

The time complexity of the above Python program is O(n), where n is the length of the input lists.
"""


def sum_list(X, Y):
    return [sum(X[i], Y[i]) for i in range(len(X))]

"""
The above Python program defines a function sum_list() which takes two lists as input and returns the sum of corresponding elements of the two lists. It returns a list containing the sum.

The function sum_list() uses a for loop to iterate over the indices of the lists and uses the built-in sum() function to calculate the sum of the elements at corresponding indices to obtain the resultant sum.

The time complexity of the above Python program is O(n), where n is the length of the input lists.
"""


```

```
def sum_list(X, Y):
    return [X[i]+Y[i] for i in range(len(X))]
```
```

def sum_list(X, Y):
    return [X[i]+Y[