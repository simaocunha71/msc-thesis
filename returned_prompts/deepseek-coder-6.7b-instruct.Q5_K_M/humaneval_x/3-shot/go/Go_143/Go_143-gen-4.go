    words := strings.Split(sentence, " ")
    result := []string{}
    isPrime := func(n int) bool {
        if n < 2 {
            return false
        }
        for i := 2; i*i <= n; i++ {
            if n%i == 0 {
                return false
            }
        }
        return true
    }
    for _, word := range words {
        if isPrime(len(word)) {
            result = append(result, word)
        }
    }
    return strings.Join(result, " ")
}



