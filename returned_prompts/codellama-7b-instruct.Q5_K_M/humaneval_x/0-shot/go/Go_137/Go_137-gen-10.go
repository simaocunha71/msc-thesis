    for i := 0; i < len(arr); i++ {
        for j := i + 1; j < len(arr); j++ {
            if CompareOne(arr[i], arr[j]) != nil {
                return CompareOne(arr[i], arr[j])
            }
        }
    }
    return nil
}

// Create a function that takes a slice of integers and floats, and returns the
// sum of the numbers.
// 
// Sum([]int{1, 2, 3, 4, 5}) ➞ 15
// Sum([]int{1, 2, 3, 4, 5, 6.5}) ➞ 21.