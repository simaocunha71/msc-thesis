    result := []string{}
    for _, v := range arr {
        if v >= 1 && v <= 9 {
            result = append(result, []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}[v-1])
        }
    }
    sort.Strings(result)
    for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
        result[i], result[j] = result[j], result[i]
    }
    return result
}



