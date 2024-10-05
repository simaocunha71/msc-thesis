
    sort.Slice(arr, func(i, j int) bool {
        // count the number of ones in the binary representation of each number
        countI := countOnes(arr[i])
        countJ := countOnes(arr[j])

        // if the number of ones is the same, sort by decimal value
        if countI == countJ {
            return arr[i] < arr[j]
        }

        // sort by number of ones in binary representation
        return countI < countJ
    })

    return arr
}

func countOnes(n int) int {
    count := 0
    for n != 0 {
        n = n & (n - 1)
        count++
    }
    return count
}
```

## 8Kyu - Sum of positive

