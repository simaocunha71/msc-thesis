    length := len(arr)
    if length <= 1 {
        return 0
    }

    left := 0
    right := length - 1

    result := 0
    while left < right {
        if arr[left] != arr[right] {
            result++
        }
        left++
        right--
    }

    return result
}



