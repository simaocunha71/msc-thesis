    count := 0
    for i, c := range s {
        if i % 2 == 0 && strings.ToUpper(string(c)) == string(c) {
            count++
        }
    }
    return count
}