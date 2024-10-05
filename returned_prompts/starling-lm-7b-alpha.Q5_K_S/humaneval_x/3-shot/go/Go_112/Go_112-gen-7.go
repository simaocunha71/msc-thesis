    result := make([]rune, 0)
    for _, char := range s {
        if !strings.Contains(c, string(char)) {
            result = append(result, char)
        }
    }
    if equal(result, reverse(result)) {
        return [2]interface{}{string(result), true}
    }else{
        return [2]interface{}{string(result), false}
    }
}


func equal(a, b []rune) bool {
    if len(a) != len(b) {
        return false
    }
    for i, char := range a {
        if char != b[i] {
            return false
        }
    }
    return true
}

func reverse(slice []rune) []rune {
    for i, j := 0, len(slice)-1; i < j; i, j = i+1, j-1 {
        slice[i], slice[j] = slice[j], slice[i]
    }
    return slice
}



