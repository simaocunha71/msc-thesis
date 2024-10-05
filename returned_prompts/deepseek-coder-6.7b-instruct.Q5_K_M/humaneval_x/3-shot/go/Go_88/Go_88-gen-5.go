    sum := array[0] + array[len(array)-1]

    sortedArray := make([]int, len(array))
    copy(sortedArray, array)

    sort.Ints(sortedArray)

    if sum % 2 == 0 {
        // Reverse the array
        for i := 0; i < len(sortedArray)/2; i++ {
            sortedArray[i], sortedArray[len(sortedArray)-1-i] = sortedArray[len(sortedArray)-1-i], sortedArray[i]
        }
    }

    return sortedArray
}



