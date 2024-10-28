
// If b equals 0 then a is the greatest common divisor
	if b == 0 {
		return a
	}

// Otherwise, find the greatest common divisor of b and a mod b
	return GreatestCommonDivisor(b, a%b)

}

