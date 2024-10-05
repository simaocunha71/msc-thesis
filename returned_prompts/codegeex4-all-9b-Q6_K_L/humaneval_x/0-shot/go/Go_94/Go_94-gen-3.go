```go
func Skjkasdkd(lst []int) int {
    maxPrime := 0
    for _, num := range lst {
        if isPrime(num) && num > maxPrime {
            maxPrime = num
        }
    }
    return sumDigits(maxPrime)
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func sumDigits(n int) int {
    sum := 0
    for n > 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}
```
这个代码的目的是找到列表中的最大质数，并返回其数字之和。首先，我们定义了一个函数`Skjkasdkd`，它接受一个整数列表作为参数。然后，我们初始化一个变量`maxPrime`为0，用于存储最大质数。接下来，我们遍历列表中的每个数字，如果数字是质数且大于当前的最大质数，则更新`maxPrime`。最后，我们调用`sumDigits`函数，将最大质数作为参数，返回其数字之和。

接下来，我们定义了一个辅助函数`isPrime`，用于判断一个数字是否为质数。如果数字小于等于1，则不是质数。否则，我们遍历从2到该数字的平方根的所有数字，如果存在一个数字能够整除该数字，则该数字不是质数。如果遍历完所有数字都没有找到能够整除的数字，则该数字是质数。

最后，我们定义了一个辅助函数`sumDigits`，用于计算一个数字的数字之和。我们使用一个循环，每次将数字除以10，并将余数加到`sum`中，直到数字变为0。最后，我们返回`sum`。

这个代码的逻辑是正确的，可以正确地找到列表中的最大质数，并返回其数字之和。