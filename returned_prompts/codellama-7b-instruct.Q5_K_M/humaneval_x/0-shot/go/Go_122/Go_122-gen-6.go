for _, v := range arr {

	if v > 99 {
		continue A
	}

	if v > 9 && v < 100 {
		continue A
	}

	if v < 10 {
		return v
	}

	return strconv.Itoa(v)

}

return 0
}
