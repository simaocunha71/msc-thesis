    sum := 0
    for i := 0; i < len(array); i++ {
        sum += array[i]
    }

    if sum % 2 == 0 {
        sort.Ints(array)
    } else {
        sort.Sort(sort.Reverse(sort.IntSlice(array)))
    }
    return array
}



