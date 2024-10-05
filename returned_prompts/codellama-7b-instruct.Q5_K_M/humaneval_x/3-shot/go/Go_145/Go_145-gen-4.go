    type Pair struct {
        Point int
        Index int
    }

    var pairs []Pair
    for i, n := range nums {
        pairs = append(pairs, Pair{Point: n, Index: i})
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].Point == pairs[j].Point {
            return pairs[i].Index < pairs[j].Index
        }
        return pairs[i].Point < pairs[j].Point
    })

    return []int{pairs[0].Index, pairs[1].Index, pairs[2].Index}
}



