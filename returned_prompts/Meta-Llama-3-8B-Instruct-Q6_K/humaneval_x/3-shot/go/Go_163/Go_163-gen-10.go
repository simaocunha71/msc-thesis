    result := make([]int, 0)
    for i := a; i <= b; i++ {
        str := strconv.Itoa(i)
        for j := 0; j < len(str); j++ {
            if str[j]%2 == 0 {
                result = append(result, i)
                break
            }
        }
    }
    return result
}