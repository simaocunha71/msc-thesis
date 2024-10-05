    var res []string
    var even []string

    for _, v := range lst {
        if len(v)%2 == 0 {
            even = append(even, v)
        }
    }

    sort.Slice(even, func(i, j int) bool {
        if len(even[i]) == len(even[j]) {
            return even[i] < even[j]
        }
        return len(even[i]) < len(even[j])
    })

    res = even
    return res
}

