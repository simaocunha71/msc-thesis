    var strArr = []string{"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
    sort.Ints(arr)
    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        arr[i], arr[j] = arr[j], arr[i]
    }
    var result = make([]string, 0)
    for _, v := range arr {
        if v >= 1 && v <= 9 {
            result = append(result, strArr[v])
        }
    }
    return result
}



