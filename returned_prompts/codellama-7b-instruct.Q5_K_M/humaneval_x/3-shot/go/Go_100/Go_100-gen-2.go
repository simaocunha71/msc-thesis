    result := make([]int, 0)
    current_level := n
    for i := 0; i < n; i++{
        result = append(result, current_level)
        if current_level%2 == 0 {
            current_level += 1
        }else{
            current_level += 2
        }
    }
    return result
}



