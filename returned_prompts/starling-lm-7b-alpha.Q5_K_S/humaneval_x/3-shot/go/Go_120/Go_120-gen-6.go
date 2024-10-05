    if len(arr) == 0 || k == 0 {
        return []int{}
    }
    sort.Ints(arr)
    return arr[:k]
}



