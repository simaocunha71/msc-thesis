    var result []int

    for i := 0; i < n; i++ {
        if n%2 == 0 {
            result = append(result, n+1)
        }else{
            result = append(result, n+2)
        }
        n = n/2
    }
    return result
}



