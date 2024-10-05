    var even_lst []string

    for _, word := range lst {
        if len(word) % 2 == 0 {
            even_lst = append(even_lst, word)
        }
    }

    sort.Slice(even_lst, func(i, j int) bool {
        return even_lst[i] < even_lst[j]
    })

    return even_lst
}



