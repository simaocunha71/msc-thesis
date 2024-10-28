    sort.Slice(array, func(i int, j int) bool {
        if array[i] + array[len(array)-1]%2 != array[j] + array[len(array)-1]%2 {
            return array[i] + array[len(array)-1]%2 < array[j] + array[len(array)-1]%2
        }
        return array[i] < array[j]
    })
    return array
}
































