    result := make([]int, 0)
    for i := a; i <= b; i++ {
        as_string := strconv.Itoa(i)
        for _, c := range as_string {
            if c - '0' % 2 == 0 {
                result = append(result, c - '0')
            }
        }
    }
    sort(result)
    return result
}



