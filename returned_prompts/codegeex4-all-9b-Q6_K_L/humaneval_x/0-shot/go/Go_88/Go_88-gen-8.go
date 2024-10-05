```go
    // create a copy of the given array
    copyArray := make([]int, len(array))
    copy(copyArray, array)
    
    // sort the copy in ascending order
    sort.Ints(copyArray)
    
    // check if the sum of the first and last elements is odd or even
    if (array[0]+array[len(array)-1])%2 == 0 {
        // if the sum is even, sort the copy in descending order
        sort.Sort(sort.Reverse(sort.IntSlice(copyArray)))
    }
    
    return copyArray
}
```