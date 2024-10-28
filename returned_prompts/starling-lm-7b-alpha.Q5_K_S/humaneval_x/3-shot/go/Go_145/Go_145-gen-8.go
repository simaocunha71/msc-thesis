    type item struct {
        value    int
        index    int
        points   int
    }

    result := make([]int, 0)
    items := make([]item, 0)

    for i, v := range nums {
        items = append(items, item{v, i, sum(v)})
    }

    sort.Slice(items, func(i, j int) bool {
        return items[i].points > items[j].points
    })

    for _, i := range items {
        result = append(result, i.value)
    }

    return result
}

func sum(num int) int {
    sum := 0
    for {
        if num < 0 {
            break
        }
        sum += (num % 10)
        num /= 10
    }
    return sum
}



