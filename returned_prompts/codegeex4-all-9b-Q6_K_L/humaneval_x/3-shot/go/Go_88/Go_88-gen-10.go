    copy_array := make([]int, len(array))
    copy(copy_array, array)

    var sum int = array[0] + array[len(array)-1]
    if sum%2 == 0 {
        sort.Slice(copy_array, func(i, j int) bool {
            return copy_array[i] > copy_array[j]
        })
    } else {
        sort.Slice(copy_array, func(i, j int) bool {
            return copy_array[i] < copy_array[j]
        })
    }

    return copy_array
}

