    var even_lst []string
    for _, str := range lst {
        if len(str) % 2 == 0 {
            even_lst = append(even_lst, str)
        }
    }

    sort.Slice(even_lst, func(i, j int) bool {
        if len(even_lst[i]) == len(even_lst[j]) {
            return even_lst[i] < even_lst[j]
        }
        return len(even_lst[i]) < len(even_lst[j])
    })

    return even_lst
}



