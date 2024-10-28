    var count int = 0
    for _, c := range s {
        if strings.ContainsRune("aeiouy", c) {
            count += 1
        }
    }
    return count
}



