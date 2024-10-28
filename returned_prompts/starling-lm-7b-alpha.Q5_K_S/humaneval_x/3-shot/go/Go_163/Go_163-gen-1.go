    result := make([]int, 0)
    for i := a; i <= b; i++ {
        s := strconv.Itoa(i)
        for j := 0; j < len(s); j++ {
            if s[j] % 2 == 0 {
                result = append(result, s[j]-'0')
            }
        }
    }
    return result
}



