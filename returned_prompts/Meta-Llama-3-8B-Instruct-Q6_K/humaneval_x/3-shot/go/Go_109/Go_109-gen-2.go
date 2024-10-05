    if len(arr) == 0 {
        return true
    }
    copy := make([]int, len(arr))
    copy = arr
    sort.Ints(copy)
    for i := 0; i < len(arr); i++ {
        for j := 0; j < len(arr)-1; j++ {
            if copy[j] > copy[j+1] {
                copy = shiftRight(copy)
            }
        }
        if !isSorted(copy) {
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

func isSorted(arr []int) bool {
    for i := 1; i < len(arr); i++ {
        if arr[i] < arr[i-1] {
            return false
        }
    }
    return true
}