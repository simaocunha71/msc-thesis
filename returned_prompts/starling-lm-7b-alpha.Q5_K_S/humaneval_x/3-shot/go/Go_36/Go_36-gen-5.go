    var count int

    for i := 1; i < n; i++ {
        if i%11 == 0 || i%13 == 0 {
            if strings.Count(strconv.Itoa(i), '7') > 0 {
                count++
            }
        }
    }
    return count
}



