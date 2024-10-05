    if len(arr) == 0 {
        return true
    }

    copy := make([]int, len(arr))
    copy = arr

    for i := 0; i < len(arr); i++ {
        sort.Ints(copy)
        if copy == arr {
            return true
        }
        rightShift(copy)
    }
    return false

}

func rightShift(arr []int) {
    last := arr[len(arr)-1]
    for i := len(arr) - 1; i > 0; i-- {
        arr[i] = arr[i-1]
    }
    arr[0] = last
}

func rightShiftHelper(arr []int, n int) {
    if n > 0 {
        last := arr[len(arr)-1]
        for i := len(arr) - 1; i > 0; i-- {
            arr[i] = arr[i-1]
        }
        arr[0] = last
        rightShiftHelper(arr, n-1)
    }
}