    result := make([]int, 0)

    for i := n; i > 0; {
        if i % 2 != 0 {
            result = append(result, i)
        }
        if i % 2 == 0 {
            i /= 2
        }else {
            i = 3 * i + 1
        }
    }
    sort.Ints(result)

    return result
}



