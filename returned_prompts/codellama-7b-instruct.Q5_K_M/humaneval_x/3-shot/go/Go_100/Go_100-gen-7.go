    result := make([]int, 0)
    i := 1
    for i <= n {
        result = append(result, i)
        if n%2 == 0{
            i = i + 1
        }else{
            i = i + 2
        }
    }
    return result
}



