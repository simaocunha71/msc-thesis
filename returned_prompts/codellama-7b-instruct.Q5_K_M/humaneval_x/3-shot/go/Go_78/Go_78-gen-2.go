    result := 0
    for _, c := range num {
        if c == 'A' || c == 'B' || c == 'E' || c == 'D' {
            result += 1
        }
    }
    return result
}



