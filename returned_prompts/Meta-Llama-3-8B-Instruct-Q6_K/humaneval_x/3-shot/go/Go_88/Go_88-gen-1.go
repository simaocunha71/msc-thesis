    copyArray := make([]int, len(array))
    copy(copyArray, array)
    sum := array[0] + array[len(array)-1]
    if sum%2 == 0 {
        sort.Reverse(sort.IntsAreLess)
    }
    sort.Ints(copyArray)
    return copyArray
}