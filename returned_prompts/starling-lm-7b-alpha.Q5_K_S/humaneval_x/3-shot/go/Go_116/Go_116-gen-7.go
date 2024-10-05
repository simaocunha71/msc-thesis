    type pair struct {
        val   int
        count int
    }

    pairs := make([]pair, 0)

    for _, v := range arr {
        pairs = append(pairs, pair{v, len(fmt.Sprintf("%b", v))})
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].count == pairs[j].count {
            return pairs[i].val < pairs[j].val
        }
        return pairs[i].count < pairs[j].count
    })

    result := make([]int, 0)
    for _, p := range pairs {
        result = append(result, p.val)
    }
    return result
}



