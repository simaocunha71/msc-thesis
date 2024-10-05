    sum := array[0] + array[len(array)-1]
    if sum % 2 == 0 {
        sort.Sort(sort.Reverse(sort.IntSlice(array)))
    } else {
        sort.Ints(array)
    }
    return array
}