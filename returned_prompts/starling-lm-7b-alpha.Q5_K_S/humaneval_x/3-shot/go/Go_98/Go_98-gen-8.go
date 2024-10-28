    count := 0
    for i, c := range s {
        if i%2 == 0 {
            if c >= 'A' && c <= 'Z' {
                count += 1
            }
        }
    }
    return count
}



