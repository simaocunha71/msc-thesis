    result := make([]int, 0)
    for i := 0; i < len(l); i++ {
        if i % 3 == 0 {
            slice := make([]int, 0)
            for _, v := range l {
                if i % 3 == 0 {
                    slice = append(slice, v)
                }
            }
            sort.Ints(slice)
            result = append(result, slice...)
        } else {
            result = append(result, l[i])
        }
    }
    return result
}