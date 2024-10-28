    upper := []rune{ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' }
    result := 0
    for i, r := range s {
        if i%2 == 0 && strings.Contains(string(upper), string(r)) {
            result++
        }
    }
    return result
}



