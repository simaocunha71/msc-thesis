    type Item struct {
        Index int
        Number int
        Points int
    }

    items := make([]Item, 0)
    for i, n := range nums {
        points := sumDigits(n)
        items = append(items, Item{i, n, points})
    }

    sort.Slice(items, func(i, j int) bool {
        return items[i].Points < items[j].Points
    })

    result := make([]int, 0)
    for _, item := range items {
        result = append(result, item.Number)
    }
    return result
}

func sumDigits(n int) int {
    s := strconv.Itoa(n)
    r, _ := strconv.Atoi(s)
    return r
}



