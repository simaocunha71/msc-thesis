    type Pair struct {
        Value int
        Index int
    }

    pairs := make([]Pair, len(arr))
    for i, v := range arr {
        pairs[i] = Pair{v, i}
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].Value == pairs[j].Value {
            return pairs[i].Index < pairs[j].Index
        }
        return pairs[i].Value < pairs[j].Value
    })

    result := make([]int, len(arr))
    for i, p := range pairs {
        result[i] = arr[p.Index]
    }

    return result
}



