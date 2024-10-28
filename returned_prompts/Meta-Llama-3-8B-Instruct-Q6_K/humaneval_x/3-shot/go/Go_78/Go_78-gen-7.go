    count := 0
    for _, c := range num {
        if c >= '2' && c <= '7' || c >= 'B' && c <= 'F' {
            count++
        }
    }
    return count
}