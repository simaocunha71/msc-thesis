    sort.Slice(arr, func(i, j int) bool {
        a, b := arr[i], arr[j]
        return countOnes(a) < countOnes(b) || (countOnes(a) == countOnes(b) && a < b)
    })
    return arr
}

func countOnes(n int) (count int) {
    for n != 0 {
        n = n & (n - 1)
        count++
    }
    return count
}

func main() {
    fmt.Println(SortArray([]int{1, 5, 2, 3, 4})) // [1, 2, 3, 4, 5]
    fmt.Println(SortArray([]int{-2, -3, -4, -5, -6})) // [-6, -5, -4, -3, -2]
    fmt.Println(SortArray([]int{1, 0, 2, 3, 4})) // [0, 1, 2, 3, 4]
}
```





## :thinking: Clarification:

This problem is asking to sort an array based on two conditions:

1. the number of ones in the binary representation of the number.
2. the decimal value of the number itself.

If the number of ones is the same, we should sort by the decimal value of the number.

## :dart: Approach:

Here is a step-by-step breakdown of the solution:

1. Define a helper function, countOnes, which takes an integer as input and returns the number of ones in its binary representation.

2. Use the sort.Slice function to sort the array. The sort.Slice function sorts the elements of a slice given a function that defines the order.

3. The function that is passed to sort.Slice should take two indices and return a boolean. It should return true if the element at the first index is less than the element at the second index, according to the conditions mentioned in the problem statement.

4. Return the sorted array.

## :rocket: Complexity:

The time complexity