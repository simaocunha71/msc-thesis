    var result []int
    for i, v := range l {
        if i%3 == 0 {
            result = append(result, v)
            sort.Ints(result)
        } else {
            result = append(result, v)
        }
    }
    return result
}



