    // copy the original array
    copiedArray := make([]int, len(array))
    copy(copiedArray, array)

    // check if the sum of the first and last elements is odd or even
    sum := copiedArray[0] + copiedArray[len(copiedArray)-1]

    // sort copied array
    sort.Ints(copiedArray)

    // if sum is even, reverse the array
    if sum%2 == 0 {
        for i := 0; i < len(copiedArray)/2; i++ {
            copiedArray[i], copiedArray[len(copiedArray)-1-i] = copiedArray[len(copiedArray)-1-i], copiedArray[i]
        }
    }