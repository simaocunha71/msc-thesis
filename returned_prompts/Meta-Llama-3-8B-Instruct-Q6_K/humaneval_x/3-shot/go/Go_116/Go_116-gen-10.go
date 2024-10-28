    type pair struct {
        val int
        ones int
    }

    pairs := make([]pair, len(arr))
    for i, val := range arr {
        pairs[i].val = val
        pairs[i].ones = binCount(val)
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].ones != pairs[j].ones {
            return pairs[i].ones < pairs[j].ones
        }
        return pairs[i].val < pairs[j].val
    })

    result := make([]int, len(arr))
    for i, pair := range pairs {
        result[i] = pair.val
    }
    return result
}

func binCount(n int) int {
    count := 0
    for n > 0 {
        n &= n - 1
        count++
    }
    return count
}