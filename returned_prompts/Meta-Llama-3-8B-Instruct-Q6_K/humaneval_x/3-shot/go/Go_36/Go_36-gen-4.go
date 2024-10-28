    count := 0
    for i := 1; i < n; i++ {
        if (i % 11 == 0 || i % 13 == 0) {
            str := strconv.Itoa(i)
            for _, char := range str {
                if string(char) == "7" {
                    count++
                }
            }
        }
    }
    return count
}