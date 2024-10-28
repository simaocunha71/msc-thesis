    even := make([]int,0)
    odd := make([]int,0)

    for _, v := range l {
        if v % 2 == 0 {
            even = append(even, v)
        }else{
            odd = append(odd, v)
        }
    }
    sort.Ints(even)
    result := append(even, odd...)
    return result
}



