    counter := 0
    for i:= 1; i < n; i++ {
        if i % 11 == 0 || i % 13 == 0 {
            counter += strings.Count(strconv.Itoa(i), "7")
        }
    }
    return counter
}



