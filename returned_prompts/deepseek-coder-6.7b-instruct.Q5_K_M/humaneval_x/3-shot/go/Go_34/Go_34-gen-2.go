    sort.Ints(l)
    result := make([]int, 0)
    last := l[0]
    result = append(result, last)
    for _, num := range l[1:] {
        if num != last {
            result = append(result, num)
            last = num
        }
    }
    return result
}



