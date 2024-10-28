    result := 0
    for i, char := range s {
        if i%2 == 0 {
            if char == 'A' || char == 'E' || char == 'I' || char == 'O' || char == 'U' {
                result += 1
            }
        }
    }
    return result
}



