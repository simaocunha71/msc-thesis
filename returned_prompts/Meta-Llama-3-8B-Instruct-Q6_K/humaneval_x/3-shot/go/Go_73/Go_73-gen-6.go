    // First, reverse the array.
    reverse_arr := make([]int, len(arr))
    copy(reverse_arr, arr)
    reverse(reverse_arr)

    // Calculate the number of changes.
    changes := 0
    for i := 0; i < len(arr); i++ {
        if arr[i] != reverse_arr[len(arr)-i-1] {
            changes++
        }
    }
    return changes
}

func reverse(arr []int) {
    left, right := 0, len(arr)-1
    for left < right {
        arr[left], arr[right] = arr[right], arr[left]
        left++
        right--
    }
}