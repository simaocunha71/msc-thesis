	var i int64 = 3
	var j int64 = 2
	var k int64 = 0
	var fib int64 = 0
	var prime int64 = 0

	if n == 0 {
		return 0
	} else if n == 1 {
		return 2
	} else if n == 2 {
		return 3
	}

	for k = 3; k < n; k++ {
		fib = i + j
		for m := int64(0); m < fib; m++ {
			if fib%m == 0 {
				prime = 0
				break
			} else {
				if m == fib-1 {
					prime = 1
				}
			}
		}
		if prime != 0 {
			break
		}
		var tmp int64 = i
		i = j
		j = tmp
	}
	return int(fib)
}




















































































































































































































































