    var firstIndex = len(array)-1
    var lastIndex = 0
    var sum = array[firstIndex]+array[lastIndex]
    if sum%2 == 0 {
        sort.Slice(array, func(i, j int) bool {
            return array[i] > array[j]
        })
    }else{
        sort.Slice(array, func(i, j int) bool {
            return array[i] < array[j]
        })
    }
    return array
}



