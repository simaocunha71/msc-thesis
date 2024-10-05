    var result int
    var element int
    var index int

    for i := 0; i < k; i++ {
        element = arr[i]
        index = strconv.Len(element)

        if index <= 2 {
            result += element
        }
    }
    return result
}



