    // Your code here
    var result []int
    for _, v := range x {
        if v%2 == 0 {
            continue A
        }
        result = append(result, v)
    }
    sort.Ints(result)
    return result
}
