    length := len(array)
    if length == 0 {
        return []int{}
    }

    firstIndex := length / 2
    lastIndex := length - 1
    if (array[firstIndex] + array[lastIndex]) % 2 == 0 {
        sort.Slice(array, func(i, j int) bool {
            return array[i] > array[j]
        })
    } else {
        sort.Slice(array, func(i, j int) bool {
            return array[i] < array[j]
        })
    }

    return array
}



