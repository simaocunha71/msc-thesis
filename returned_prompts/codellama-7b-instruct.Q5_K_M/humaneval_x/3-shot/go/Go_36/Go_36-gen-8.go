    result := 0
    for i := 1; i < n; i++ {
        if (i % 11 == 0 || i % 13 == 0) && strings.Contains(strconv.Itoa(i), "7") {
            result += 1
        }
    }
    return result
}



