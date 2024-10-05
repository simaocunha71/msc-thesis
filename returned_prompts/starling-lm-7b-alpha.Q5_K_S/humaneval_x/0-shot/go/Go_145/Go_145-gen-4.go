    var res []int

    type pair struct {
        v    int
        idx  int
    }

    numsCopy := make([]int, len(nums))
    for i, n := range nums {
        numsCopy[i] = n
    }

    type bySum struct {
        v int
    }
    type byIndex struct {
        idx int
    }

    for _, n := range nums {
        sum := 0
        for i := 0; i < len(strconv.Itoa(n)); i++ {
            sum += int(strconv.Itoa(n)[i] - '0')
        }
        res = append(res, pair{sum, i})
    }
    sort.Slice(res, func(i, j int) bool {
        if res[i].v == res[j].v {
            return res[i].idx < res[j].idx
        }
        return res[i].v < res[j].v
    })

    for _, p := range res {
        numsCopy[p.idx] = nums[p.idx]
    }

    return numsCopy
}





































































































































































































































