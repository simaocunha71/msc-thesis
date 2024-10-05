    type item struct {
        num int
        idx int
    }
    items := make([]item, len(nums))
    for i, n := range nums {
        items[i] = item{n, i}
    }
    sort.Slice(items, func(i, j int) bool {
        return items[i].num + items[i].idx < items[j].num + items[j].idx
    })
    result := make([]int, len(nums))
    for i, item := range items {
        result[item.idx] = item.num
    }
    return result
}



