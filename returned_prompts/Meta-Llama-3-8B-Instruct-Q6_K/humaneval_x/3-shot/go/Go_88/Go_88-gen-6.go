    copy_of_array := make([]int, len(array))
    copy_of_array = append(copy_of_array, array...)
    sum := array[0] + array[len(array)-1]
    if sum % 2 == 0 {
        sort.Sort(sort.Reverse(sort.IntSlice(copy_of_array)))
    } else {
        sort.Ints(copy_of_array)
    }
    return copy_of_array
} 