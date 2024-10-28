    n := len(arr)
    var left, right int
    var changes int
    var half int

    // find the middle of the array
    half = n / 2

    // if the array is odd, the middle element will be a part of the first half
    if n % 2 != 0 {
        half -= 1
    }

    // iterate from the start to the middle
    left = half
    for left >= 0 {
        if arr[left] != arr[n-left-1] {
            changes += 1
        }
        left -= 1
    }

    // iterate from the end to the middle
    right = half + 1
    for right < n {
        if arr[right] != arr[n-right-1] {
            changes += 1
        }
        right += 1
    }

    return changes
}