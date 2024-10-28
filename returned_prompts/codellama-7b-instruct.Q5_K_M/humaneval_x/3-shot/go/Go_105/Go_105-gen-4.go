    result := make([]int, len(arr))
    copy(result, arr)
    sort.Ints(result)
    names := []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
    names_map := make(map[int]string)
    for i, num := range names{
        names_map[i+1] = num
    }

    for i, num := range result {
        if num > 0 && num < 10 {
            result[i] = names_map[num]
        }else{
            result[i] = 0
        }
    }
    return result
}



