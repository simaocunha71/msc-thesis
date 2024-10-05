    var count int
    s = strings.ToUpper(s)
    for i, c := range s {
        if i % 2 == 0 && (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            count += 1
        }
    }
    return count
}



