    // sort the array
    sort.Ints(array)

    // find the sum of the first and last element
    sum := array[0] + array[len(array)-1]

    // if the sum is odd, sort in ascending order
    if sum%2 == 1 {
        return array
    }

    // if the sum is even, sort in descending order
    for i := len(array)/2 - 1; i >= 0; i-- {
        j := len(array) - i - 1
        array[i], array[j] = array[j], array[i]
    }

    return array
}
