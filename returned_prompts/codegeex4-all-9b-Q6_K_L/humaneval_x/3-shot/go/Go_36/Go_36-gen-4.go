    count := 0
    for i := 0; i < n; i++ {
        if i%11 == 0 || i%13 == 0 {
            s := strconv.Itoa(i)
            count += strings.Count(s, "7")
        }
    }
    return count
}



