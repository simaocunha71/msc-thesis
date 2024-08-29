```python
def sum_common_divisors(n1, n2):
    def common_divisors(n):
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        return divisors

    return sum(set(common_divisors(n1)) & set(common_divisors(n2)))

print(sum_common_divisors(10,15))  # 6
```

