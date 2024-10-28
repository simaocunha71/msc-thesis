    result := make([]int, 0)
    for i := a; i <= b; i++ {
        str := strconv.Itoa(i)
        for _, c := range str {
            if c % 2 == 0 {
                result = append(result, i)
                break
            }
        }
    }
    return result
}