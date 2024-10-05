    sortedArr := make([]int, len(arr))
    copy(sortedArr, arr)
    sort.Ints(sortedArr)

    for i := 0; i < len(arr); i++ {
        if isNonDecreasing(shift(sortedArr, i)) {
            return true
        }
    }
    return false
}

func shift(arr []int, s int) []int {
    return append(arr[len(arr)-s:], arr[:len(arr)-s]...)
}

func isNonDecreasing(arr []int) bool {
    for i := 0; i < len(arr)-1; i++ {
        if arr[i] > arr[i+1] {
            return false
        }
    }
    return true
}


