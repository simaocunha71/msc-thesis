    result := make([]int, 0)
    for _, number := range numbers {
        if !contains(result, number) {
            result = append(result, number)
        }
    }
    return result
}

func contains(slice []int, value int) bool {
    for _, v := range slice {
        if v == value {
            return true
        }
    }
    return false
}



