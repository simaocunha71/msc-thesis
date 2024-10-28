
// Start by checking if the number is less than 2, if it is then it can't be prime.
if n < 2 {
return false
}

// Check for divisibility by 2
if n%2 == 0 {
return n == 2
}

// Check for divisibility by all odd numbers up to the square root of n
i := 3
for i*i <= n {
if n%i == 0 {
return false
}
i += 2
}

return true
}
*/

func IsPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n%2 == 0 {
		return n == 2
	}

	i := 3
	for i*i <= n {
		if n%i == 0 {
			return false
		}
		i += 2
	}

	return true
}

/*
func IsPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n%2 == 0 {
		return n == 2
	}

	i := 3
	for i*i <= n {
		if n%i == 0 {
			return false
		}
		i += 2
	}

	return true
}
*/

/*
func IsPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}

	i := 3
	for i*i <= n {
		if n%i == 0 {
			return false
		}
		i += 2
	}

	return true
}
*/

/*
func IsPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n%2 == 0 {
		return false
	}

	i := 3
	for i*i <= n {
		if n%i == 0 {
			return false
		}
		i += 2
	}

	return true
}
*/

/*
func IsPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n%2