    sortedArr := make([]int, len(arr))
    copy(sortedArr, arr)
    sort.Ints(sortedArr)

    for i := 0; i < len(arr); i++ {
        if isNonDecreasing(arr) {
            return true
        }
        arr = append(arr[len(arr)-1:], arr[:len(arr)-1]...)
    }
    return false
}

func isNonDecreasing(arr []int) bool {
    for i := 0; i < len(arr)-1; i++ {
        if arr[i] > arr[i+1] {
            return false
        }
    }
    return true
}



