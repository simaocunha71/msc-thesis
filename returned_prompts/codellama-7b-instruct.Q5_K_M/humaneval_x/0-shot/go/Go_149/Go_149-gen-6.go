    var list []string

    for _, v := range lst {
        if len(v)%2 == 0 {
            list = append(list, v)
        }
    }

    sort.Strings(list)

    return list
}
