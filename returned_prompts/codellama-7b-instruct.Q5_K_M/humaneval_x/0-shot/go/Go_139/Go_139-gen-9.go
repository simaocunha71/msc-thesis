
// The factorial of zero is defined as 1.
// So when n is zero, we return 1.
if n == 0 {
	return 1
}

// We multiply the n! by the result of the function called with n-1.
return n * SpecialFactorial(n-1)

}