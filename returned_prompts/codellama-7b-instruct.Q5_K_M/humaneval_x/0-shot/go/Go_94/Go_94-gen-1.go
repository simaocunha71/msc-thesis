	for _, v := range lst {
		if v > 1 {
			for i := 2; i < math.Sqrt(float64(v)); i++ {
				if v%i == 0 {
					continue A
				}
			}
			return strconv.Atoi(string(v))
		}
	}
	return 0
}

