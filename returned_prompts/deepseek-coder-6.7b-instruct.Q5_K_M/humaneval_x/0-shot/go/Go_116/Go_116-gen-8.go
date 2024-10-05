
sort.Slice(arr, func(i, j int) bool {
    // count ones in binary representation of each number
    countI := countOnes(arr[i])
    countJ := countOnes(arr[j])

    // if the count is the same, sort by the decimal values
    if countI == countJ {
        return arr[i] < arr[j]
    }
    // otherwise, sort by the count
    return countI < countJ
})
return arr
}

func countOnes(n int) (count int) {
    for n != 0 {
        n = n & (n - 1)
        count++
    }
    return
}

Explanation:
In the function `SortArray`, we use `sort.Slice` to sort the array in-place. The sort order is defined by the function passed to `sort.Slice`.

For each pair of elements (i, j), if the count of ones in their binary representations is the same, we sort them based on their decimal values. Otherwise, we sort them based on the count of ones in their binary representations.

The function `countOnes` uses bitwise operations to count the number of ones in the binary representation of a number. It keeps reducing the number by one until it becomes zero. The number of operations it takes is the count of ones in the binary representation of the number.

This solution has time complexity O(n log n), where n is the size of the input array. The space complexity is O(n), because we are storing the array in-place.

Note: This solution assumes that the input array is non-negative. If the input array can have negative numbers, then a different approach may be needed to count the number of ones in the binary representation of the number.

Also, the `countOnes` function may not work as expected for negative numbers because of the way negative numbers are represented in binary. A different approach may be needed to count the number of ones in the binary representation of the number.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
