    count := 0
    for i, c := range s {
        if string(c) == strings.ToUpper(string(c)) && i%2 == 0 {
            count += 1
        }
    }
    return count
}



