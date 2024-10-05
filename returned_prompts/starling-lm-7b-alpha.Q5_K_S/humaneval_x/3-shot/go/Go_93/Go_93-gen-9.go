    result := make([]rune, 0)
    for _, c := range message {
        if c >= 'A' && c <= 'Z' {
            result = append(result, (c + 13) % 26 + 'A')
        }else if c >= 'a' && c <= 'z' {
            result = append(result, (c + 13) % 26 + 'a')
        }
    }
    vowels := "aeiou"
    for _, c := range result {
        if strings.Contains(vowels, string(c)) {
            index := 2
            if c == 'u' {
                index = 3
            }
            result = append(result, vowels[index % 5]+string(c))
        }
    }
    return string(result)
}



