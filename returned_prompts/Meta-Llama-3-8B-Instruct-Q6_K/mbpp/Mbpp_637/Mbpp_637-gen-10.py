```
def noprofit_noloss(price, amount):
    if amount > price:
        return False
    else:
        return True
```
The function `noprofit_noloss` takes two parameters, `price` and `amount`. It checks if the `amount` is greater than the `price`. If it is, it means there is a profit, so it returns `False`. If not, it means there is no profit or no loss, so it returns `True`. The unit test `assert noprofit_noloss(1500,1200)==False` suggests that if the amount is greater than the price, there is a profit, so the function should return `False`. 

For example, if the price of a stock is 1500 and you sell it for 1200, you have a loss. The function should return `True` in this case. But if you buy it for 1200 and sell it for 1500, you have a profit, so the function should return `False`. 