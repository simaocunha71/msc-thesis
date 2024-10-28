    for i, word := range strings.Split(sentence, " ") {
        if !isPrime(len(word)) {
            continue A
        }
    }
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