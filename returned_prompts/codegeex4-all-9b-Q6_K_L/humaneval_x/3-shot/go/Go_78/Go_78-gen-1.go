    count := 0
    for _, c := range num {
        if c == '2' || c == '3' || c == '5' || c == '7' || c == 'B' || c == 'D' {
            count += 1
        }
    }
    return count
}



