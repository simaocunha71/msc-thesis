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

    words := strings.Split(sentence, " ")
    result := make([]string, 0, len(words))

    for _, word := range words {
        if isPrime(len(word)) {
            result = append(result, word)
        }
    }

    return strings.Join(result, " ")
}



