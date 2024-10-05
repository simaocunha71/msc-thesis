    type pair struct {
        val int
        cnt int
    }

    result := make([]pair, 0)
    for _, v := range arr {
        result = append(result, pair{v, countOnes(v)})
    }
    sort.Slice(result, func(i, j int) bool {
        if result[i].cnt == result[j].cnt {
            return result[i].val < result[j].val
        }
        return result[i].cnt < result[j].cnt
    })

    res := make([]int, 0)
    for _, p := range result {
        res = append(res, p.val)
    }
    return res
}

func countOnes(n int) int {
    cnt := 0
    for n > 0 {
        cnt += n % 2
        n >>= 1
    }
    return cnt
}



