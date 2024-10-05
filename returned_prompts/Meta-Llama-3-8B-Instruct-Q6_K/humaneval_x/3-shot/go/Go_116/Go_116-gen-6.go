    type Pair struct {
        val int
        ones int
    }
    pairs := make([]Pair, len(arr))
    for i, v := range arr {
        pairs[i].val = v
        pairs[i].ones = binOnes(v)
    }
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].ones == pairs[j].ones {
            return pairs[i].val < pairs[j].val
        }
        return pairs[i].ones < pairs[j].ones
    })
    result := make([]int, len(arr))
    for i, v := range pairs {
        result[i] = v.val
    }
    return result
}

func binOnes(n int) int {
    count := 0
    for n > 0 {
        n = n & (n - 1)
        count++
    }
    return count
}
} 