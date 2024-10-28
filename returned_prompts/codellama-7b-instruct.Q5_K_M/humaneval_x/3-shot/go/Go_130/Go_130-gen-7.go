    result := make([]float64, 0)

    if n == 0 {
        return result
    }

    if n == 1 {
        return []float64{1}
    }

    if n == 2 {
        return []float64{1, 3, 2}
    }

    if n % 2 == 0 {
        return append([]float64{1, 3, 2}, Tri(n - 1)...)
    }

    return append(Tri(n - 1), Tri(n - 2)...)
}



