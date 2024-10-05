    var names = []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
    var result = []string{}

    sort.Ints(arr)

    for i := len(arr) - 1; i >= 0; i-- {
        if arr[i] > 0 && arr[i] < 10 {
            result = append(result, names[arr[i]-1])
        }
    }

    return result
}



