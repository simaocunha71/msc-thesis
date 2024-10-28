    var result int
    for i := 11; i < n; i += 11 {
        if strings.Contains(strconv.Itoa(i), "7") {
            result += 1
        }
    }

    for i := 13; i < n; i += 13 {
        if strings.Contains(strconv.Itoa(i), "7") {
            result += 1
        }
    }
    return result
}



