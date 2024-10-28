    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i] - numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}


