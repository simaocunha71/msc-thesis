    sum := array[0] + array[len(array) - 1]
    result := make([]int, len(array))
    copy(result, array)
    sort.Ints(result)

    if sum % 2 == 0 {
        for i, j := 0, len(result) - 1; i < j; i, j = i + 1, j - 1 {
            result[i], result[j] = result[j], result[i]
        }
    }

    return result
}



