    result := make([]string, 0)

    words := strings.Split(sentence, " ")
    for _, word := range words {
        is_prime := true
        for i := 2; i < len(word); i++ {
            if len(word)%i == 0 {
                is_prime = false
                break
            }
        }
        if is_prime {
            result = append(result, word)
        }
    }
    return strings.Join(result, " ")
}



