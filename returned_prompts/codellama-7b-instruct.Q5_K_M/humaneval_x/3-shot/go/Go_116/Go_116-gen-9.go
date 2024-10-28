    type pair struct {
        value int
        key int
    }

    var pairs []pair

    for _, v := range arr {
        var key int
        for i := 0; i < 32; i++ {
            if v&(1<<uint(i)) > 0 {
                key += 1 << uint(i)
            }
        }
        pairs = append(pairs, pair{key:key, value:v})
    }

    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].key == pairs[j].key {
            return pairs[i].value < pairs[j].value
        }
        return pairs[i].key < pairs[j].key
    })
    return pair_sort(pairs)
}

func pair_sort(pairs []pair) []int {
    result := make([]int, len(pairs))
    for i, v := range pairs {
        result[i] = v.value
    }
    return result
}



