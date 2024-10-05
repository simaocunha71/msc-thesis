    var result []string
    m := make(map[int][]string)

    for _, word := range lst {
        if len(word)%2 == 0 {
            m[len(word)] = append(m[len(word)], word)
        }
    }

    for key := range m {
        sort.Strings(m[key])
        result = append(result, m[key]...)
    }

    sort.Slice(result, func(i, j int) bool {
        return result[i] < result[j]
    })

    return result
}



