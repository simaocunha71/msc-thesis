    sortedArr  := make([]int, len(arr))
    copy(sortedArr, arr)
    sort.Ints(sortedArr)

    for i := range arr {
        if isShiftedSorted(arr, sortedArr, i) {
            return true
        }
    }
    return false
}

func isShiftedSorted(arr, sortedArr []int, shift int) bool {
    for i := range arr {
        if arr[(i+shift)%len(arr)] != sortedArr[i] {
            return false
        }
    }
    return true
}



