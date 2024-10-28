    result := make([]string, 0)
    current_count := 0
    for _, r := range s {
        if r != ' ' {
            if !is_vowel(r) {
                current_count += 1
            }
            if current_count == n {
                result = append(result, strings.Trim(s, " "))
            }
        }
    }
    return result
}

func is_vowel(c rune) bool {
    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'y'}
    return bytes.IndexByte(vowels, c) >= 0
}



