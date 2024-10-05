    names := []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
    var result []string

    for _, v := range arr {
        if v >= 1 && v <= 9 {
            result = append(result, names[v-1])
        }
    }

    sort.Slice(result, func(i, j int) bool {
        return len(result[i]) > len(result[j])
    })
    result = reverse(result)
    return result
}

func reverse(s []string) []string {
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
    return s
}