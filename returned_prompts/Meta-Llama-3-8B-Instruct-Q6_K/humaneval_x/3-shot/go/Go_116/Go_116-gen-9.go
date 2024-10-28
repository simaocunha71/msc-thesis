    type pair struct {
        num int
        ones int
    }
    result := make([]int, 0)
    pairs := make([]pair, 0)

    for _, num := range arr {
        ones := 0
        temp := num
        for temp > 0 {
            temp = temp / 2
            ones += temp % 2
        }
        pairs = append(pairs, pair{num, ones})
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].ones == pairs[j].ones {
            return pairs[i].num < pairs[j].num
        }
        return pairs[i].ones < pairs[j].ones
    })

    for _, pair := range pairs {
        result = append(result, pair.num)
    }
    return result
}