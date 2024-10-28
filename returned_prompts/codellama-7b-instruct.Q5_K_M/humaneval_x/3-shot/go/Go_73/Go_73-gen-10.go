    // reverse the array
    var reverse []int = make([]int, len(arr))
    for i, j := 0, len(arr)-1; i < len(arr); i, j = i+1, j-1 {
        reverse[i] = arr[j]
    }

    // find the first index that has a different value
    var min int = 0
    var i, j int = 0, 0
    for i, j = 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        if arr[i] != reverse[j] {
            min = i + 1
            break
        }
    }

    // find the number of elements to change
    return len(arr) - min
}



