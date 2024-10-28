    if (array[0] + array[len(array)-1]) % 2 == 0 {
        sort.Slice(array, func(i, j int) bool {
            return array[i] > array[j]
        })
    }else {
        sort.Slice(array, func(i, j int) bool {
            return array[i] < array[j]
        })
    }
    return array
}



