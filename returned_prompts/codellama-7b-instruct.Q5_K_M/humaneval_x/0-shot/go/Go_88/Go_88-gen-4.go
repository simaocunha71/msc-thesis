    sort.Ints(array)

    sum := 0
    for i := range array {
        sum += array[i]
    }

    if sum%2 == 0 {
        sort.Reverse(sort.IntSlice(array))
    }
    return array
}
