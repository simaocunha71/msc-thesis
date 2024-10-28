    if n < 0 {
        panic("Negative numbers are not allowed")
    }

    if n == 0 {
        return []float64{1}
    }

    if n == 1 {
        return []float64{1, 3}
    }

    if n == 2 {
        return []float64{1, 3, 2}
    }

    result := []float64{1, 3, 2}
    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            result = append(result, 1.0+float64(i)/2)
        } else {
            result = append(result, result[i-1]+result[i-2]+result[i-3])
        }
    }
    return result
}



