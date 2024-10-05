    type pair struct {
        num int
        sum int
        index int
    }

    pairs := make([]pair, len(nums))
    for i, n := range nums {
        pairs[i] = pair{n, sumDigits(n), i}
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].sum == pairs[j].sum {
            return pairs[i].index < pairs[j].index
        }
        return pairs[i].sum < pairs[j].sum
    })

    result := make([]int, len(nums))
    for i, p := range pairs {
        result[i] = nums[p.index]
    }
    return result
}

func sumDigits(n int) int {
    result := 0
    for n > 0 {
        result += n % 10
        n /= 10
    }
    return result
}


















