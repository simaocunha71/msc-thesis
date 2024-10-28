    words := strings.Split(sentence, " ")
    primes := []string{}
    for _, word := range words {
        if isPrime(len(word)) {
            primes = append(primes, word)
        }
    }
    return strings.Join(primes, " ")
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

// 解题思路：
// 首先，我们需要将句子分割成单词。我们可以使用strings.Split函数来实现。
// 然后，我们需要遍历每个单词，并检查其长度是否为素数。
// 如果是素数，我们将其添加到一个新的切片中。
// 最后，我们将新的切片使用strings.Join函数连接成一个字符串，并返回。
// 判断一个数是否为素数的函数isPrime会检查该数是否有除了1和它本身以外的因数。
// 如果有，那么它就不是素数；如果没有，那么它就是素数。
// 这个函数会检查到该数的平方根为止的因数，因为一个更大的因数会是已经检查过的较小因数的倍数。
// 如果这个数小于2，那么它就不是素数。
//