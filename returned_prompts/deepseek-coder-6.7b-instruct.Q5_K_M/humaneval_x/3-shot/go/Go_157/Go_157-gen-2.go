    sides := []int{a, b, c}
    sort.Ints(sides)

    return math.Pow(float64(sides[0]), 2) + math.Pow(float64(sides[1]), 2) == math.Pow(float64(sides[2]), 2)
}



