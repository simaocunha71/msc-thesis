    if n == 1 {
        return []float64{1}
    }

    if n%2 == 0{
        result := []float64{3}
        for i := 0; i < n-2; i++{
            result = append(result, result[i] + result[i+1] + result[i+2])
        }
        return result
    }

    result := []float64{1}
    for i := 0; i < n-1; i++{
        result = append(result, result[i] + result[i+1] + result[i+2])
    }
    return result
}



