    count := 0
    for i := 1; i < n; i++ {
        if i%11 == 0 || i%13 == 0 {
            num := strconv.Itoa(i)
            if strings.Count(num, "7") > 0 {
                count++
            }
        }
    }
    return count
}



