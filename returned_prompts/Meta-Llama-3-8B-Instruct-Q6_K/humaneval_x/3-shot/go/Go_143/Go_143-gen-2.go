    words := strings.Split(sentence, " ")
    result := ""
    for _, word := range words {
        if isPrime(len(word)) {
            result += word + " "
        }
    }
    return strings.TrimSpace(result)
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