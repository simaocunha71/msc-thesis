    count := 0
    for _, c := range num {
        switch {
        case c >= '2' && c <= '7':
            count++
        case c == 'B':
            count++
        case c == 'D':
            count++
        }
    }
    return count
}