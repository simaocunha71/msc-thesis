    if n == 0 {
        return []float64{1}
    } else if n == 1 {
        return []float64{1, 3}
    } else if n == 2 {
        return []float64{1, 3, 2}
    }

    result := Tri(n - 1)
    result = append(result, result[len(result)-1]+result[len(result)-2]+result[len(result)-3])

    return result
}

