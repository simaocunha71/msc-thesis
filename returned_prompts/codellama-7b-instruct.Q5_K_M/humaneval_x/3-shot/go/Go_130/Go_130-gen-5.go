    result := make([]float64, 0)

    if n == 0 {
        return result
    }

    result = append(result, 1.0)

    if n == 1 {
        return result
    }

    result = append(result, 3.0)

    if n == 2 {
        return result
    }

    if n % 2 == 0 {
        result = append(result, Tri(n - 1)...)
        result = append(result, Tri(n - 2)...)
    }else {
        result = append(result, Tri(n - 1)...)
        result = append(result, Tri(n - 2)...)
        result = append(result, Tri(n + 1)...)
    }

    return result
}



