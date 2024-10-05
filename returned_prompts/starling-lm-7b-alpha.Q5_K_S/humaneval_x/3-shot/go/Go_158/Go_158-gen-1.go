    var result string
    var max_count int

    for _, w := range words {
        temp_set := make(map[rune]bool)
        for _, c := range w {
            temp_set[c] = true
        }
        set_size := len(temp_set)
        if set_size > max_count || (set_size == max_count && w < result) {
            result = w
            max_count = set_size
        }
    }

    return result
}



