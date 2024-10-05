    type pair struct {
        val  int
        idx int
    }
    t := make([]pair, len(nums))
    for i, v := range nums {
        t[i] = pair{v, i}
    }
    sort.Slice(t, func(i, j int) bool {
        return t[i].val+t[j].val < t[j].val+t[i].val ||
               t[i].val+t[j].val == t[j].val+t[i].val && t[i].idx < t[j].idx
    })
    ret := make([]int, len(nums))
    for i := range ret {
        ret[i] = t[i].val
    }
    return ret
}


func OrderByPoints(nums []int) []int {
    type pair struct {
        val  int
        idx int
    }
    t := make([]pair, len(nums))
    for i, v := range nums {
        t[i] = pair{v, i}
    }
    sort.Slice(t, func(i, j int) bool {
        return t[i].val+t[j].val < t[j].val+t[i].val ||
               t[i].val+t[j].val == t[j].val+t[i].val && t[i].idx < t[j].idx
    })
    ret := make([]int, len(nums))
    for i := range ret {
        ret[i] = t[i].val
    }
    return ret
}
































































































































