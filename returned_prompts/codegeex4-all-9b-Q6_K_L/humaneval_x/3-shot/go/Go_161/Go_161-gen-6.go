    var result []rune = make([]rune, 0)
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result = append(result, c-'a'+'A')
        } else if c >= 'A' && c <= 'Z' {
            result = append(result, c-'A'+'a')
        } else {
            result = append(result, c)
        }
    }
    for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
        result[i], result[j] = result[j], result[i]
    }
    return string(result)
}

