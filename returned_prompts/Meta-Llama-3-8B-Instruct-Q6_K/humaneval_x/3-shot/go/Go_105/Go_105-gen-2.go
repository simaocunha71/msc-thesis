    names := [...]string{"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
    result := make([]string, 0)
    var filtered []int

    for _, num := range arr {
        if num >= 1 && num <= 9 {
            filtered = append(filtered, num)
        }
    }

    sort.Ints(filtered)
    for i := len(filtered) - 1; i >= 0; i-- {
        result = append(result, names[filtered[i]])
    }

    return result
}