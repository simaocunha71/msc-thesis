    words := strings.Split(sentence," ")
    prime_words := make([]string,0)

    for _,word := range words{
        if isPrime(len(word)){
            prime_words = append(prime_words,word)
        }
    }

    return strings.Join(prime_words," ")
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n <= 3 {
        return true
    }
    if n%2 == 0 || n%3 == 0 {
        return false
    }
    i := 5
    for i*i <= n {
        if n%i == 0 || n%(i+2) == 0 {
            return false
        }
        i += 6
    }
    return true
}



