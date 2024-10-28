    sum := array[0] + array[len(array)-1]
    var sorted_array []int
    if sum%2 == 0 {
        sorted_array = append(sorted_array, array...)
        sort.Sort(sort.Reverse(sort.IntSlice(sorted_array)))
    } else {
        sorted_array = append(sorted_array, array...)
        sort.Ints(sorted_array)
    }
    return sorted_array
}