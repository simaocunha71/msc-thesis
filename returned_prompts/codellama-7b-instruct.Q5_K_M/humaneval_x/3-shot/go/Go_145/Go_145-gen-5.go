    type Pair struct {
        Index int
        DigitsSum int
    }

    pairs := make([]Pair, len(nums))

    for i, num := range nums {
        pairs[i].Index = i
        pairs[i].DigitsSum = 0
        for num > 0 {
            pairs[i].DigitsSum += num % 10
            num /= 10
        }
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].DigitsSum == pairs[j].DigitsSum {
            return pairs[i].Index < pairs[j].Index
        }
        return pairs[i].DigitsSum < pairs[j].DigitsSum
    })

    result := make([]int, len(nums))
    for i, pair := range pairs {
        result[i] = nums[pair.Index]
    }
    return result
}



