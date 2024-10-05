    n := len(arr)
    left := 0
    right := n - 1

    for left < right {
        if arr[left] != arr[right] {
            return n - 1
        }
        left++
        right--
    }
    return 0
}
}
}}


