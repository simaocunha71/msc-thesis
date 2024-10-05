    vowels := []rune{'a','e','i','o','u'}
    result := make([]rune, 0)
    for _, c := range message {
        if c >= 'a' && c <= 'z' {
            if strings.Contains(vowels, c) {
                result = append(result, vowels[(c-'a'+2)%5+'a'])
            } else {
                result = append(result, (c+32)/32)
            }
        } else if c >= 'A' && c <= 'Z' {
            result = append(result, (c+32)/32)
        }
    }

    return string(result)
}




