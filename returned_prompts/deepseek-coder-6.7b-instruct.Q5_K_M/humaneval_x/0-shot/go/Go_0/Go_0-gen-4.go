    for i := range numbers {
        for _, w := range numbers[i+1:] {
            if math.Abs(numbers[i]-w)