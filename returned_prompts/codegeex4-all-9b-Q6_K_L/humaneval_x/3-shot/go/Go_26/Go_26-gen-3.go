    result := make([]int, 0)
    for _, n := range numbers{
        if !Contains(result, n){
            result = append(result, n)
        }
    }
    return result
}

func Contains(numbers []int, value int) bool {
    for _, n := range numbers {
        if n == value {
            return true
        }
    }
    return false
}



