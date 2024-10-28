    n := len(arr)
    left := 0
    right := n - 1

    for left < right {
        if arr[left] != arr[right] {
            break
        }
        left += 1
        right -= 1
    }

    var changes int
    for i := 0; i < left; i++ {
        if arr[i] != arr[n - 1 - i] {
            changes++
        }
    }
    for i := left + 1; i < right; i++ {
        changes++
    }
    return changes
}