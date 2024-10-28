    result := make([]int, 0)
    for i := a; i <= b; i++ {
        for _, digit := range strconv.Itoa(i) {
            if digit == '2' || digit == '4' || digit == '6' || digit == '8' {
                result = append(result, i)
                break
            }
        }
    }
    sort.Ints(result)
    return result
}