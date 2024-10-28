    names := map[int]string{1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    arr = append([]int{}, arr...)
    sort.Ints(arr)
    arr = arr[::-1]
    result := make([]string, 0)
    for _, v := range arr {
        if v < 10 {
            result = append(result, names[v])
        }
    }
    return result
}



