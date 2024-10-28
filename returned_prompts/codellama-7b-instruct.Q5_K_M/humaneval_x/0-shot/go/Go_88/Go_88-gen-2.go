    // 1. Check if the array is empty
    if len(array) == 0 {
        return []int{}
    }

    // 2. Sort the array
    sort.Ints(array)

    // 3. Check the sum of the first and last index
    sum := array[0] + array[len(array)-1]

    // 4. Return the sorted array
    return array
}
