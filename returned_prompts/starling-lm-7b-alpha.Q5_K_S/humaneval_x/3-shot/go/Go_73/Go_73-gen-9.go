    left, right := 0, len(arr)-1

    while left < right {
        if arr[left] != arr[right] {
            left++
        } else {
            right--
        }
    }

    return left + right
}



