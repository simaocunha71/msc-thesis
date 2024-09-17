```
def noprofit_noloss(amount, cost):
    return amount == cost
```


The problem asks to write a function that checks if a given amount has no profit and no loss. The function takes two parameters: the amount and the cost. The function should return True if the amount is equal to the cost, meaning there is no profit or loss, and False otherwise.

The unit test `assert noprofit_noloss(1500,1200)==False` suggests that the function should return False when the amount is greater than the cost, which means there is a profit. Therefore, we can conclude that the function should return True only when the amount is equal to the cost, and False otherwise.

Here is the solution:
```
def noprofit_noloss(amount, cost):
    return amount == cost
```
This function uses the equality operator (==) to compare the amount with the cost. If they are equal, it returns True, indicating no profit or loss. Otherwise, it returns False, indicating either a profit or a loss.