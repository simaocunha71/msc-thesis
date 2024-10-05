    count := 0
    for i := 11; i < n; i += 11 {
        count += strings.Count(strconv.Itoa(i), "7")
    }
    for i := 13; i < n; i += 13 {
        count += strings.Count(strconv.Itoa(i), "7")
    }
    return count
}