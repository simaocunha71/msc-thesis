	x, err := strconv.ParseFloat(value, 64)
	if err != nil {
		panic(err)
	}

	y := math.Round(x)

	if x-y == 0 {
		return int(y)
	}

	if x-y < 0 {
		return int(y - 1)
	}

	return int(y + 1)
}
























