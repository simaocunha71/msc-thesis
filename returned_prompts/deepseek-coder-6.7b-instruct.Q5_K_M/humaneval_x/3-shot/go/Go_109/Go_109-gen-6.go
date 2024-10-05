    sortedArr  := make([]int, len(arr))
    copy(sortedArr, arr)
    sort.Ints(sortedArr)

    for i  := 0; i < len(arr); i++  {
        if isShiftedSorted(arr, sortedArr)  {
            return true
        }
        arr = shiftRight(arr)
    }
    return false
}

func isShiftedSorted(arr, sortedArr []int) bool  {
    for i  := 0; i < len(arr); i++  {
        if arr[i]  != sortedArr[i]  {
            return false
        }
    }
    return true
}

func shiftRight(arr []int) []int  {
    last := arr[len(arr)-1]
    for i  := len(arr) - 1; i > 0; i--  {
        arr[i] = arr[i-1]
    }
    arr[0] = last
    return arr
}



