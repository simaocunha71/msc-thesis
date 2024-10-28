    sum := array[0] + array[len(array)-1]
    copyArray := make([]int, len(array))
    copy(copyArray, array)
    sort.Ints(copyArray)
    if sum % 2 == 0 {
        for i, j := 0, len(copyArray)-1; i < j; i, j = i+1, j-1 {
            copyArray[i], copyArray[j] = copyArray[j], copyArray[i]
        }
    }
    return copyArray
}



