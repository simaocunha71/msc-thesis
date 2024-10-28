
def count_up_to(n):
    if n < 2:
        return []
    if n < 3:
        return [2]
    primes = [2,3]
    for i in range(3,n):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True



# print(count_up_to(20))
# print(count_up_to(1))
# print(count_up_to(3))
# print(count_up_to(5))
# print(count_up_to(11))
# print(count_up_to(18))





```
？

上述代码定义了一个函数 `count_up_to(n)`，它接受一个非负整数 `n` 作为参数，并返回一个包含第 `n` 个素数以下的素数列表的数组。例如，`count_up_to(5)` 将返回 `[2,3]`，`count_up_to(11)` 将返回 `[2,3,5,7]` 等等。

函数 `count_up_to(n)` 首先检查参数 `n` 是否小于 2。如果是，则返回一个空数组。如果 `n` 等于 2，则返回一个包含单个素数 2 的数组。如果 `n` 大于 2 并且小于 3，则返回一个包含单个素数 2 和 3 的数组。

接下来，函数初始化一个 `primes` 列表，包含素数 2 和 3。然后，从 3 到 `n` 的每个数字 `i` 进行检查。函数调用 `is_prime(