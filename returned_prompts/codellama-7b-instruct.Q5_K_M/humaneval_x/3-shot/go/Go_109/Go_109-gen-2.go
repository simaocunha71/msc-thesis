    if len(arr) == 0 {
        return true
    }

    // Sort the array in non-decreasing order
    sort.Ints(arr)
    // Get the last element of the array
    last_element := arr[len(arr)-1]
    // Get the first element of the array
    first_element := arr[0]
    // If the last element is greater than first element, then
    // it is not possible to get sorted array
    if last_element > first_element {
        return false
    }

    // Get the difference between last element and first element
    diff := last_element - first_element
    // Iterate over the array
    for i := 1; i < len(arr); i++ {
        // Check if the current element is greater than previous
        // element by 'diff'
        if arr[i] > arr[i-1] + diff {
            return false
        }
    }

    return true
}



