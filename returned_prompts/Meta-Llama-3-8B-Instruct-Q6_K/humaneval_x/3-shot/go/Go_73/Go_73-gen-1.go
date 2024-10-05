    // Create a copy of the array
    arrCopy := make([]int, len(arr))
    copy(arrCopy, arr)

    // Reverse the copy of the array
    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        arrCopy[i], arrCopy[j] = arrCopy[j], arrCopy[i]
    }

    // Count the number of elements that need to be changed
    changed := 0
    for i := 0; i < len(arr); i++ {
        if arr[i] != arrCopy[i] {
            changed++
        }
    }

    return changed
} 