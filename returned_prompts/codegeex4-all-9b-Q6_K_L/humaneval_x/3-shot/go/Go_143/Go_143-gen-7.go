    words := strings.Split(sentence, " ")
    prime_words := make([]string, 0)

    for _, word := range words {
        if IsPrime(len(word)) {
            prime_words = append(prime_words, word)
        }
    }
    return strings.Join(prime_words, " ")
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i < int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}