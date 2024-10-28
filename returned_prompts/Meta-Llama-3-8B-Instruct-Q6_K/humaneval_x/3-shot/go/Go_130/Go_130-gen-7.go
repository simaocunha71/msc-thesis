    if n == 0 {
        return []float64{}
    } else if n == 1 {
        return []float64{3.0}
    } else if n == 2 {
        return []float64{1.0, 3.0}
    } else {
        result := []float64{1.0, 3.0}
        for i := 3; i <= n; i++ {
            var next float64
            if i % 2 == 0 {
                next = 1.0 + float64(i)/2
            } else {
                next = result[i-1] + result[i-2] + result[i-3]
            }
            result = append(result, next)
        }
        return result
    }
}