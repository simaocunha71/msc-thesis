    sortedArr := make([]int, len(arr))
    copy(sortedArr, arr)
    sort.Ints(sortedArr)
    for i := 0; i < len(arr); i++ {
        if isSame(arr, sortedArr) {
            return true
        }
        arr = shiftRight(arr)
    }
    return false
}

func isSame(a, b []int) bool {
    if len(a) != len(b) {
        return false
    }
    for i, v := range a {
        if v != b[i] {
            return false
        }
    }
    return true
}

func shiftRight(arr []int) []int {
    last := arr[len(arr)-1]
    for i := len(arr) - 1; i > 0; i-- {
        arr[i] = arr[i-1]
    }
    arr[0] = last
    return arr
}



