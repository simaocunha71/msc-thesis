
def eat(number, need, remaining):
    total = number + need
    remaining -= total
    if remaining < 0:
        remaining = 0
    return [total, remaining]


if __name__ == "__main__":
    print(eat(5, 6, 10))  # [11, 4]
    print(eat(4, 8, 9))  # [12, 1]
    print(eat(1, 10, 10))  # [11, 0]
    print(eat(2, 11, 5))  # [7, 0]

```
