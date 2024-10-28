    if len(xs) % 2 == 1 {
        return []float64{}
    }

    // find the largest non-zero coefficient
    max_coeff_idx := 0
    for i := 1; i < len(xs); i++ {
        if math.Abs(float64(xs[i])) > math.Abs(float64(xs[max_coeff_idx])) {
            max_coeff_idx = i
        }
    }

    // find the roots
    var roots []float64
    for i := 0; i < len(xs)-1; i++ {
        if xs[i] != 0 {
            var root float64
            var err float64
            for j := 0; j < 10;