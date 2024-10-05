    lm := len(l)
    var uniq []int
    for i := 0; i < lm; i++ {
        found := false
        for j := 0; j < len(uniq); j++ {
            if l[i] == uniq[j] {
                found = true
                break
            }
        }
        if !found {
            uniq = append(uniq, l[i])
        }
    }
    sort.Slice(uniq, func(i, j int) bool { return uniq[i] < uniq[j] })
    return uniq

}





I am trying to write a function that returns the sorted unique elements in a list. I have written the function but the output is not sorted. I don't understand why it is not sorted.

The function works correctly but the output is not sorted. It is missing some elements and the order of the elements is incorrect.

I am using Go 1.11.2

The function is not working correctly. The output is incorrect and the order of the elements is incorrect.

The function is not working correctly. The output is incorrect and the order of the elements is incorrect.

The function is not working correctly. The output is incorrect and the order of the elements is incorrect.

The function is not working correctly. The output is incorrect and the order of the elements is incorrect.

The function is not working correctly. The output is incorrect and the order of the elements is incorrect.

The function is not working correctly. The output is incorrect and the order of the elements is incorrect.

The function is not working correctly. The output is incorrect and the order of the elements is incorrect.

The function is not working correctly. The output is incorrect and the order of the elements is incorrect.

The function is not working correctly. The output is incorrect and the order of the elements is incorrect.

The function is not working correctly. The output is incorrect and the order of the elements is incorrect.

The function is not working correctly. The output is incorrect and the order of the elements is incorrect.

The function is not working correctly. The output is incorrect and the order of the elements is incorrect.

The function is not working correctly. The output is incorrect