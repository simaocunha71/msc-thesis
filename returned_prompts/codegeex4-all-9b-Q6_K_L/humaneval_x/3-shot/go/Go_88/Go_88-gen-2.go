    result := make([]int, len(array))
    copy(result, array)

    if (array[0] + array[len(array)-1]) % 2 == 0 {
        sort.Slice(result, func(i, j int) bool {
            return result[i] > result[j]
        })
    } else {
        sort.Slice(result, func(i, j int) bool {
            return result[i] < result[j]
        })
    }

    return result
}

