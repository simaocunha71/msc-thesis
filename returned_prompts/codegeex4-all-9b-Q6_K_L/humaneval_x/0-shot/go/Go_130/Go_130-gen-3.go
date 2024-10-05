func Tri(n int) []float64 {
    if n == 0 {
        return []float64{3}
    }
    if n == 1 {
        return []float64{1, 3}
    }
    if n == 2 {
        return []float64{1, 3, 2}
    }
    if n == 3 {
        return []float64{1, 3, 2, 8}
    }
    if n > 3 {
        result := []float64{1, 3, 2, 8}
        for i := 4; i <= n; i++ {
            if i%2 == 0 {
                result = append(result, float64(1)+float64(i)/2)
            } else {
                result = append(result, result[i-1]+result[i-2]+result[i-3])
            }
        }
        return result
    }
    return []float64{}
}