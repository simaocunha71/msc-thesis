    sum := 0

    for _, n := range lst {
        if n < 0 {
            continue
        }

        if math.Mod(n, 2) == 1 {
            sum += int(math.Pow(n, 2))
        }
    }

    return sum
}



