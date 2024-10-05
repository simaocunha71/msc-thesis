    var count int
    for i := 11; i < n; i += 11 {
        if strings.Contains(strconv.Itoa(i), "7") {
            count++
        }
    }
    for i := 13; i < n; i += 13 {
        if strings.Contains(strconv.Itoa(i), "7") {
            count++
        }
    }
    return count
}

