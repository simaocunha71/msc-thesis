    result := make([]int, len(l))
    for i := 0; i < len(l); i++ {
        result[i] = l[i]
    }

    sort.Slice(result[0:], func(i int, j int) bool {
        return (i+1)%2 == 0 && (j+1)%2 == 0 && result[i] > result[j]
    })

    return result
}



