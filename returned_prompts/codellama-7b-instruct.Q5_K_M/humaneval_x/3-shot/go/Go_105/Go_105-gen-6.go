    names := []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
    sort.Ints(arr)
    arr = reverse(arr)
    result := make([]string, 0)
    for _, a := range arr {
        if a > 0 && a < 10 {
            result = append(result, names[a - 1])
        }
    }
    return result
}

func reverse(arr []int) []int {
    for i, j := 0, len(arr) - 1; i < j; i, j = i + 1, j - 1 {
        arr[i], arr[j] = arr[j], arr[i]
    }
    return arr
}



