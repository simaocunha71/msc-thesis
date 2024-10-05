
// Return a greatest common divisor of two integers a and b
// >>> GreatestCommonDivisor(3, 5)
// 1
// >>> GreatestCommonDivisor(25, 15)
// 5
func GreatestCommonDivisor(a int,b int) int{

	if a == 0{
		return b
	}
	if b == 0{
		return a
	}
	for a != b{
		if a > b{
			a -= b
		}else{
			b -= a
		}
	}
	return a
}
