    sort.Slice(arr, func(i, j int) bool {
        countI := 0
        countJ := 0
        for _, b := range fmt.Sprintf("%b", arr[i]) {
            if b == '1' {
                countI++
            }
        }
        for _, b := range fmt.Sprintf("%b", arr[j]) {
            if b == '1' {
                countJ++
            }
        }
        if countI == countJ {
            return arr[i] < arr[j]
        }
        return countI < countJ
    })
    return arr
}



