    count := 0
    vowels := []rune{'A', 'E', 'I', 'O', 'U'}
    for i := 0; i < len(s); i += 2 {
        for _, v := range vowels {
            if s[i] == v {
                count++
                break
            }
        }
    }
    return count
}



