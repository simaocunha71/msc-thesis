    partsX := strings.Split(x, "/")
    partsN := strings.Split(n, "/")

    numX, _ := strconv.Atoi(partsX[0])
    numN, _ := strconv.Atoi(partsN[0])
    denX, _ := strconv.Atoi(partsX[1])
    denN, _ := strconv.Atoi(partsN[1])

    return (float64(numX * denN) == float64(numN * denX))
}



