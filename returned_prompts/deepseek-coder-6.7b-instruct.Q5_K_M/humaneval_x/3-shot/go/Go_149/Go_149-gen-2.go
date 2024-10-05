    var even_lst  []string
    for _, word := range lst {
        if len(word) % 2 == 0 {
            even_lst = append(even_lst, word)
        }
    }
    sort.Strings(even_lst)
    return even_lst
}



