```
def noprofit_noloss(cost, selling):
    return cost == selling
```


The function `noprofit_noloss` takes two parameters: `cost` and `selling`. It checks if the `cost` is equal to the `selling` amount. If they are equal, it returns `False` because there is neither a profit nor a loss. If they are not equal, it returns `True`. This is based on the unit test `assert noprofit_noloss(1500,1200)==False`, which implies that there is a loss when the selling amount is less than the cost. The function does not consider the profit or loss percentage. It only checks if there is a profit or loss. If there is no profit or loss, it returns `False`. If there is a profit or loss, it returns `True`.