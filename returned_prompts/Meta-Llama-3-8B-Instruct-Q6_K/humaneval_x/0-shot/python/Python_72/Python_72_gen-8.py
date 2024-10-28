```
def will_it_fly(q, w):
    if str(q) == str(q)[::-1]:
        return sum(q) <= w
    else:
        return False
``` 