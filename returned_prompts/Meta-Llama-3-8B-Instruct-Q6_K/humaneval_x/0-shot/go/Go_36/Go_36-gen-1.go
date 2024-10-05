    count := 0
    for i := 1; i < n; i++ {
        if strings.Contains(strconv.Itoa(i), "7") {
            if i%11 == 0 || i%13 == 0 {
                count++
            }
        }
    }
    return count
}

