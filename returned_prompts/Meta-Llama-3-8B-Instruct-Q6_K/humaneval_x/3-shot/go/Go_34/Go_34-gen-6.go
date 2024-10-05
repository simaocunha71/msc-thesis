    var unique []int
    for _, i := range l {
        exists := false
        for _, j := range unique {
            if i == j {
                exists = true
                break
            }
        }
        if !exists {
            unique = append(unique, i)
        }
    }
    sort.Ints(unique)
    return unique
}