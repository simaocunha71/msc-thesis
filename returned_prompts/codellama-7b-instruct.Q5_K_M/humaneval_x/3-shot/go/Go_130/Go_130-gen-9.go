    result := make([]float64, 0)
    for i := 0; i <= n; i++ {
        if i == 1 {
            result = append(result, 1)
        }else if i % 2 == 0 {
            result = append(result, 1 + float64(i) / 2)
        }else{
            result = append(result, Tri(i-1) + Tri(i-2) + Tri(i+1))
        }
    }
    return result
}



