    if len(arr) == 0 {
        return true
    }

    // Find the index of the minimum element
    minIndex := 0
    for i, num := range arr {
        if num < arr[minIndex] {
            minIndex = i
        }
    }

    // Check if the minimum element is at the last position
    if minIndex == len(arr)-1 {
        return true
    }

    // Check if the array is already sorted
    if sort.IntsAreSorted(arr) {
        return true
    }

    // Check if the minimum element can be moved to the last position by right shifting
    for i := minIndex + 1; i < len(arr); i++ {
        if arr[i] < arr[i-1] {
            return false
        }
    }

    return true
}


