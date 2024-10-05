    result := make([]int, 0)
    for _, number := range numbers {
        if !contain(result, number) {
            result = append(result, number)
        }
    }
    return result
}

func contain(slice []int, value int) bool {
    for _, v := range slice {
        if v == value {
            return true
        }
    }
    return false
}




