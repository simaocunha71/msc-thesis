    var result []float64

    // find the smallest and largest numbers
    smallest := math.Inf(1)
    largest := math.Inf(-1)
    for _, num := range numbers {
        if num < smallest {
            smallest = num
        }
        if num > largest {
            largest = num
        }
    }

    // create a scaling factor
    scale := 1 / (largest - smallest)

    // apply the scaling factor to each number
    for _, num := range numbers {
        result = append(result, (num - smallest) * scale)
    }

    return result
}


