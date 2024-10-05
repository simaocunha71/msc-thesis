    n := len(arr)
    center := n / 2
    left := center - 1
    right := center + 1

    if n == 1 {
        return 0
    }

    count := 0

    for left >= 0 && right < n {
        if arr[left] == arr[right] {
            left -= 1
            right += 1
        } else {
            count += 1
            left -= 1
            right += 1
            for left >= 0 && arr[left] != arr[right] {
                count += 1
                left -= 1
            }
        }
    }

    return count
}



