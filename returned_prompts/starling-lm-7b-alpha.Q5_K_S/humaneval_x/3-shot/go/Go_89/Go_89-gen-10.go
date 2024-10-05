    result := make([]rune, 0)
    for _, c := range s {
        c_rotated := c + 2*2
        if c_rotated > 'z' {
            c_rotated -= 26
        }
        result = append(result, c_rotated)
    }
    return string(result)
}



