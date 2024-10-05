
	xn, xd := strings.Split(x, "/"), strings.Split(n, "/")
	xn1, xd1 := strconv.Atoi(xn[0]), strconv.Atoi(xn[1])
	xn2, xd2 := strconv.Atoi(xd[0]), strconv.Atoi(xd[1])
	xn3, xd3 := xn1*xd2, xn2*xd1

	if xn3 == xd3 {
		return true
	}
	return false
}
