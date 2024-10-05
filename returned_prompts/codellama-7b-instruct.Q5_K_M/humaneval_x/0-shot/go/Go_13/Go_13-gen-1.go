
// Return a greatest common divisor of two integers a and b
// >>> GreatestCommonDivisor(3, 5)
// 1
// >>> GreatestCommonDivisor(25, 15)
// 5
func GreatestCommonDivisor(a int,b int) int{

	if a == 0{
		return b
	}else if b == 0{
		return a
	}
	for a > 0 && b > 0{
		if a < b{
			b = b % a
		}else{
			a = a % b
		}
	}
	return a + b
}


// Return a greatest common divisor of two integers a and b
// >>> GreatestCommonDivisor(3, 5)
// 1
// >>> GreatestCommonDivisor(25, 15)
// 5
func GreatestCommonDivisor(a int,b int) int{

	if a == 0{
		return b
	}else if b == 0{
		return a
	}
	for a > 0 && b > 0{
		if a < b{
			b = b % a
		}else{
			a = a % b
		}
	}
	return a + b
}


// Return a greatest common divisor of two integers a and b
// >>> GreatestCommonDivisor(3, 5)
// 1
// >>> GreatestCommonDivisor(25, 15)
// 5
func GreatestCommonDivisor(a int,b int) int{

	if a == 0{
		return b
	}else if b == 0{
		return a
	}
	for a > 0 && b > 0{
		if a < b{
			b = b % a
		}else{
			a = a % b
		}
	}
	return a + b
}


// Return a greatest common divisor of two integers a and b
// >>>