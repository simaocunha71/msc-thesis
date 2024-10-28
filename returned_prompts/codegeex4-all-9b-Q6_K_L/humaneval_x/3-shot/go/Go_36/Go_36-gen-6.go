    result := 0
    for i := 0; i < n; i++ {
        if i%11 == 0 || i%13 == 0 {
            str := strconv.Itoa(i)
            for _, c := range str {
                if c == '7' {
                    result += 1
                }
            }
        }
    }
    return result
}



