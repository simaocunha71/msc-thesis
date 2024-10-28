    var result []string
    var buffer bytes.Buffer
    vowels := []rune{'a', 'e', 'i', 'o', 'u'}

    for _, r := range s {
        if r == ' ' {
            if len(buffer) == n {
                for _, r := range buffer.String() {
                    if !contains(vowels, r) {
                        n--
                    }
                }
                if n == 0 {
                    result = append(result, buffer.String())
                }
            }
            buffer.Reset()
        }else if !contains(vowels, r) {
            buffer.WriteRune(r)
        }
    }
    return result
}

func contains(slice []rune, element rune) bool {
    for _, a := range slice {
        if a == element {
            return true
        }
    }
    return false
}



