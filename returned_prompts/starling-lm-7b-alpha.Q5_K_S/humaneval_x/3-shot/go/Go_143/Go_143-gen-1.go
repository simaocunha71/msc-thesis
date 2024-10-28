    var result strings.Builder
    for _, word := range strings.Fields(sentence) {
        if isPrime(len(word)) {
            result.WriteString(word+" ")
        }
    }
    return result.String()[:len(result.String())-1]
}

func isPrime(n int) bool {
    if n <= 3 {
        return n > 1
    }
    for i := 2; i * i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}



