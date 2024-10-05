
    return int(math.Pow(2, float64(n))) % p
}

*/

import "math"

func Modp(n int, p int) int {
	return int(math.Pow(2, float64(n))) % p
}

// Modp2 is the same as Modp but with the use of Pow2 and Modulus
func Modp2(n, p int) int {
	return Pow2(n) % p
}

// Pow2 returns 2^n
func Pow2(n int) int {
	return 1 << uint(n)
}

// Modp3 is the same as Modp but with the use of Pow2 and Modulus
func Modp3(n, p int) int {
	return Pow2(n) % p
}

// Modp4 is the same as Modp but with the use of Pow2 and Modulus
func Modp4(n, p int) int {
	return Pow2(n) % p
}

// Modp5 is the same as Modp but with the use of Pow2 and Modulus
func Modp5(n, p int) int {
	return Pow2(n) % p
}

// Modp6 is the same as Modp but with the use of Pow2 and Modulus
func Modp6(n, p int) int {
	return Pow2(n) % p
}

// Modp7 is the same as Modp but with the use of Pow2 and Modulus
func Modp7(n, p int) int {
	return Pow2(n) % p
}

// Modp8 is the same as Modp but with the use of Pow2 and Modulus
func Modp8(n, p int) int {
	return Pow2(n) % p
}

// Modp9 is the same as Modp but with the use of Pow2 and Modulus
func Modp9(n, p int) int {
	return Pow2(n) % p
}

// Modp10 is the same as Modp but with the use of Pow2 and Modulus
func Modp10(n, p int) int {
	return Pow2(n) % p
