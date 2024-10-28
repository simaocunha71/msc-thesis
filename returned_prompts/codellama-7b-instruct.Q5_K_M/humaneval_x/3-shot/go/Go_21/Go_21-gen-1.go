    var min_val float64 = math.MaxFloat64
    var max_val float64 = math.SmallestNonzeroFloat64

    for _, number := range numbers {
        min_val = math.Min(min_val, number)
        max_val = math.Max(max_val, number)
    }

    var result []float64 = make([]float64, len(numbers))

    for i, number := range numbers {
        result[i] = (number-min_val)/(max_val-min_val)
    }
    return result
}



