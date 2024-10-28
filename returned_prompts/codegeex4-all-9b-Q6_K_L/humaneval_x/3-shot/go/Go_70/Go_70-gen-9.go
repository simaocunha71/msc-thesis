    sort.Ints(lst)
    result := make([]int, len(lst))

    for i, j := 0, 0; i < len(lst); i++ {
        if i%2 == 0 {
            result[i] = lst[j]
            j++
        } else {
            result[i] = lst[len(lst)-j]
        }
    }

    return result
}

