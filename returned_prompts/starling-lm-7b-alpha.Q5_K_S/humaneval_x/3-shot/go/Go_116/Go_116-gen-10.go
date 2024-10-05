    type Pair struct {
        Value   int
        Ones    int
    }

    pairs := make([]Pair, len(arr))
    for i, v := range arr {
        pairs[i] = Pair{Value: v, Ones: countOnes(v)}
    }
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].Ones != pairs[j].Ones {
            return pairs[i].Ones < pairs[j].Ones
        }
        return pairs[i].Value < pairs[j].Value
    })
    result := make([]int, len(arr))
    for i, pair := range pairs {
        result[i] = pair.Value
    }
    return result
}

func countOnes(n int) int {
    result := 0
    for ; n > 0; n /= 2 {
        result += n % 2
    }
    return result
}



