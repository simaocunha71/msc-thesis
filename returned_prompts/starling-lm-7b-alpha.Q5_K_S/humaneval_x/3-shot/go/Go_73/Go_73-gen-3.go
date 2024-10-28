    length := len(arr)
    if length <= 1 {
        return 0
    }

    // Calculate the palindromic array
    palindromic := make([]int, length)
    for i := 0; i < length/2; i++ {
        palindromic[i] = palindromic[length-1-i] = arr[i]
    }

    // Count number of changes needed to make the array palindromic
    changes := 0
    for i := 0; i < length; i++ {
        if palindromic[i] != arr[i] {
            changes += 1
        }
    }
    return changes
}



