    if n == 0 {
        return []float64{1}
    } else if n == 1 {
        return []float64{1, 3}
    } else if n == 2 {
        return []float64{1, 3, 2}
    }

    sequence := make([]float64, n+1)
    sequence[0] = 1
    sequence[1] = 3
    sequence[2] = 2

    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            sequence[i] = 1 + float64(i)/2
        } else {
            sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i+1]
        }
    }

    return sequence
}



