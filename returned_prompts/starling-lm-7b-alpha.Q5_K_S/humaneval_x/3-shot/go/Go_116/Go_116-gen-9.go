    type pair struct {
        val int
        one int
    }
    result := make([]int, 0)
    tmp := make([]pair, 0)
    for _, v := range arr {
        tmp = append(tmp, pair{v, countOnes(v)})
    }
    sort.Slice(tmp, func(i, j int) bool {
        if tmp[i].one != tmp[j].one {
            return tmp[i].one < tmp[j].one
        }
        return tmp[i].val < tmp[j].val
    })
    for _, v := range tmp {
        result = append(result, v.val)
    }
    return result
}

func countOnes(n int) int {
    result := 0
    for ; n != 0; result += 1, n >>= 1)
    return result
}



