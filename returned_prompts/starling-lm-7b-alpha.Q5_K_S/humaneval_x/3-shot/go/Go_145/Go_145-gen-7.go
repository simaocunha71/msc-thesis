    type item struct {
        num int
        s   int
        i   int
    }

    items := make([]item, 0, len(nums))
    for i, n := range nums {
        items = append(items, item{n, sum(n), i})
    }
    sort.Slice(items, func(i, j int) bool {
        return items[i].s < items[j].s || (items[i].s == items[j].s && items[i].i < items[j].i)
    })
    result := make([]int, 0, len(items))
    for _, item := range items {
        result = append(result, item.num)
    }
    return result
}

func sum(n int) int {
    r := 0
    for n > 0 {
        r += n % 10
        n /= 10
    }
    return r
}



