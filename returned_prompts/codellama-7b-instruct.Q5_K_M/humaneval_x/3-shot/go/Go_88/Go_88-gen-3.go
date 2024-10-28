    var sum int = 0
    for _, element := range array {
        sum += element
    }

    if sum % 2 == 0 {
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



