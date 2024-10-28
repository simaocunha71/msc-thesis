    sortedArr := make([]int, len(arr))
    copy(sortedArr, arr)
    sort.Ints(sortedArr)

    for i := range arr {
        if isSorted(arr) {
            return true
        }
        arr = rotateRight(arr)
    }
    return false
}

func rotateRight(arr []int) []int {
    last := arr[len(arr)-1]
    for i := len(arr) - 1; i > 0; i-- {
        arr[i] = arr[i-1]
    }
    arr[0] = last
    return arr
}

func isSorted(arr []int) bool {
    for i := 0; i < len(arr)-1; i++ {
        if arr[i] > arr[i+1] {
            return false
        }
    }
    return true
}



