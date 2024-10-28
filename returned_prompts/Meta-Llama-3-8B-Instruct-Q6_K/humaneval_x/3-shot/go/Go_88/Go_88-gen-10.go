    sum := array[0] + array[len(array)-1]
    copyArray := make([]int, len(array))
    copy(array, copyArray)
    if sum%2 == 0 {
        sort.Sort(sort.Reverse(sort.IntSlice(copyArray)))
    } else {
        sort.Ints(copyArray)
    }
    return copyArray
}