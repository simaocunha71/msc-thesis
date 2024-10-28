    copy_array := make([]int, 0)
    copy_array = append(copy_array, array...)

    if (array[0] + array[len(array) - 1]) % 2 == 0 {
        sort.Slice(copy_array, func(i, j int) bool {
            return copy_array[i] > copy_array[j]
        })
    }else {
        sort.Slice(copy_array, func(i, j int) bool {
            return copy_array[i] < copy_array[j]
        })
    }

    return copy_array
}

