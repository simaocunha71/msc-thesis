```
def noprofit_noloss(cost, amount):
    return amount >= cost
```


In this function, we are checking if the given amount is greater than or equal to the cost. If it is, then there is no profit or loss, and the function returns True. If the amount is less than the cost, then there is a loss, and the function returns False. This function passes the given unit test. 

The unit test `assert noprofit_noloss(1500,1200)==False` is also passing as expected. The amount 1200 is less than the cost 1500, so the function returns False, indicating a loss. 





The unit test `assert noprofit_noloss(1500,1500)==True` will also pass. The amount 1500 is equal to the cost 1500, so the function returns True, indicating no profit or loss.