    count := 0
    for i := 1; i < n; i++ {
        if i % 11 == 0 || i % 13 == 0 {
            count += strings.Count(strconv.Itoa(i), "7")
        }
    }
    return count
}

