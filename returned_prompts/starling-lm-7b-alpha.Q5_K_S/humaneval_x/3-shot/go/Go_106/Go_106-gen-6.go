    result := make([]int, 0)
    for i:= 1; i <= n; i++ {
        if i % 2 == 0 {
            result = append(result, math.Factorial(i))
        }else {
            result = append(result, SumOfFirstN(i))
        }
    }
    return result
}



