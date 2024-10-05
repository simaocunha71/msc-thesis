    count := 0
    for _, c := range num {
        switch c {
        case '2', 'B':
            count++
        case '3', 'D':
            count++
        case '5', '7':
            count++
        }
    }
    return count
}