    result := make([]int, 0)
    for i := 0; i < len(l); i++ {
        if i % 3 == 0 {
            temp := make([]int, 0)
            for _, v := range l {
                if v % 3 == 0 {
                    temp = append(temp, v)
                }
            }
            sort.Ints(temp)
            result = append(result, temp...)
        } else {
            result = append(result, l[i])
        }
    }
    return result
}