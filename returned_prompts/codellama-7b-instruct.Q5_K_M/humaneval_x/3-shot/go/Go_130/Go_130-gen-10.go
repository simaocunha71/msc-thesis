    result := make([]float64, 0)

    if n < 0{
        return result
    }

    if n == 0{
        return []float64{1}
    }

    if n == 1{
        return []float64{1, 3}
    }

    if n == 2{
        return []float64{1, 3, 2}
    }

    result = append(result, 1)

    var temp1, temp2 float64 = 0, 3

    for i := 3; i <= n; i++ {
        result = append(result, temp1)
        temp1 = temp2
        temp2 = result[i - 1] + result[i - 2] + result[i - 3]
    }

    return result
}



