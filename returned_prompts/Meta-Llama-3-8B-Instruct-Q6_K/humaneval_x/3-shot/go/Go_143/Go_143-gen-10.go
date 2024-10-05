    words := strings.Split(sentence, " ")
    var result strings.Builder

    for _, word := range words {
        if isPrime(len(word)) {
            result.WriteString(word + " ")
        }
    }

    return strings.TrimSpace(result.String())
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