
// Return a greatest common divisor of two integers a and b
// >>> GreatestCommonDivisor(3, 5)
// 1
// >>> GreatestCommonDivisor(25, 15)
// 5
func GreatestCommonDivisor(a,b int) int{

	// If a == b, return a
	if a == b{
		return a
	}

	// If a == 0, return b
	if a == 0{
		return b
	}

	// If b == 0, return a
	if b == 0{
		return a
	}

	// If a is odd, return GreatestCommonDivisor(b, a)
	if a % 2 != 0{
		return GreatestCommonDivisor(b, a)
	}

	// If b is odd, return GreatestCommonDivisor(a, b)
	if b % 2 != 0{
		return GreatestCommonDivisor(a, b)
	}

	// If a and b are even, return GreatestCommonDivisor(a / 2, b / 2) * 2
	return GreatestCommonDivisor(a / 2, b / 2) * 2
}
```