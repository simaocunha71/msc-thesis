    count := 0
    for i, c := range s {
        if strings.Contains("AEIOU", string(c)) && i%2 == 0 {
            count += 1
        }
    }
    return count
}



