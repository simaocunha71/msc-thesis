    var result []string

    // Remove odd length strings
    for _, item := range lst {
        if len(item)%2 == 0 {
            result = append(result, item)
        }
    }

    // Sort by length and alphabet
    sort.Slice(result, func(i, j int) bool {
        if len(result[i]) != len(result[j]) {
            return len(result[i]) < len(result[j])
        }
        return result[i] < result[j]
    })

    return result
}


func SortedListSum(lst []string) []string {
    var result []string
    for _, item := range lst {
        if len(item)%2 == 0 {
            result = append(result, item)
        }
    }
    sort.Slice(result, func(i, j int) bool {
        if len(result[i]) != len(result[j]) {
            return len(result[i]) < len(result[j])
        }
        return result[i] < result[j]
    })
    return result
}





func SortedListSum(lst []string) []string {
    result := []string{}
    for _, item := range lst {
        if len(item)%2 == 0 {
            result = append(result, item)
        }
    }
    sort.Slice(result, func(i, j int) bool {
        if len(result[i]) != len(result[j]) {
            return len(result[i]) < len(result[j])
        }
        return result[i] < result[j]
    })
    return result
}





func SortedListSum(lst []string) []string {
    result := []string{}
    for _, item := range lst {
        if len(item)%2 == 0 {
            result = append(result, item)
        }
    }
    sort.Slice(result, func(i, j int) bool {
        if len(result[i]) != len(result[j]) {
           