    // Create a pair list to store the sum of digits and index of each number
    pairList := make([]pair, len(nums))
    for i, num := range nums {
        sum := 0
        if num < 0 {
            num = -num
        }
        for num > 0 {
            digit := num % 10
            sum += digit
            num /= 10
        }
        pairList[i] = pair{sum, i}
    }

    // Sort the pair list by the sum of digits and then by index
    sort.Slice(pairList, func(i, j int) bool {
        if pairList[i].sum == pairList[j].sum {
            return pairList[i].index < pairList[j].index
        }
        return pairList[i].sum < pairList[j].sum
    })

    // Construct the sorted number list
    sortedNums := make([]int, len(nums))
    for i, pair := range pairList {
        sortedNums[i] = nums[pair.index]
    }

    return sortedNums
}

type pair struct {
    sum   int
    index int
}
```

## 2. 题目2：
