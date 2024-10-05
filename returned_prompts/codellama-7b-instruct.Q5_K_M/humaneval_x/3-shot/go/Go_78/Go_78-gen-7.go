    var count int = 0

    for _, digit := range num {
        if digit == 'A' || digit == 'B' || digit == 'E' || digit == 'D' {
            count += 1
        }
    }
    return count
}



