```
def noprofit_noloss(selling, buying):
    return selling <= buying
```


This function takes two parameters, `selling` and `buying`, which represent the selling price and buying price of a product, respectively. It returns `False` if the selling price is less than or equal to the buying price, indicating no profit and no loss. Otherwise, it returns `True`.

The unit test `assert noprofit_noloss(1500,1200)==False` suggests that if the selling price is 1500 and the buying price is 1200, there is a profit, so the function should return `False`.

Note that this function assumes that the selling and buying prices are positive. If negative prices are possible, additional checks would be needed. 