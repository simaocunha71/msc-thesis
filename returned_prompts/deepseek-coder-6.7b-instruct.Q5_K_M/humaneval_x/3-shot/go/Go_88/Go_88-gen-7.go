    sum := array[0] + array[len(array)-1]
    sortedArray := make([]int, len(array))
    copy(sortedArray, array)
    sort.Ints(sortedArray)

    if sum%2 == 0 {
        for i, j := 0, len(sortedArray)-1; i < j; i, j = i+1, j-1 {
            sortedArray[i], sortedArray[j] = sortedArray[j], sortedArray[i]
        }
    }
    return sortedArray
}



