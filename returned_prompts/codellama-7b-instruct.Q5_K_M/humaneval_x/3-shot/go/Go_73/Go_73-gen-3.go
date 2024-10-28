    var min_changes int = 0
    var is_palindrome bool = true

    for i := 0; i < len(arr); i++ {
        if i < len(arr)-1-i {
            if arr[i] != arr[len(arr)-1-i] {
                is_palindrome = false
                break A
            }
        }
    }

    if is_palindrome {
        return min_changes
    }

    for i := 0; i < len(arr); i++ {
        for j := i+1; j < len(arr); j++ {
            if arr[i] != arr[j] {
                min_changes += 1
            }
        }
    }
    return min_changes
}



