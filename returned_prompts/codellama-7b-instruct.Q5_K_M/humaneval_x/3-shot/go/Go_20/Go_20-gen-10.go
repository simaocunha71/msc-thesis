    var closest [2]float64

    for i := 0; i < len(numbers) - 1; i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i] - numbers[j]) < math.Abs(closest[1] - closest[0]) {
                closest[0] = numbers[i]
                closest[1] = numbers[j]
            }
        }
    }
    return closest
}



