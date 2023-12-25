
// Your task is to write a function that returns true if a number x is a simple
// power of n and false in other cases.
// x is a simple power of n if n**int=x
// For example:
// IsSimplePower(1, 4) => true
// IsSimplePower(2, 2) => true
// IsSimplePower(8, 2) => true
// IsSimplePower(3, 2) => false
// IsSimplePower(3, 1) => false
// IsSimplePower(5, 3) => false
func IsSimplePower(x int,n int) bool {
	if x == 0 || n == 0 { return true } // If one of the arguments is zero (or both), return instantly.

	var f = float64(x); // Store as a floating point value to avoid integer overflow later on.

	for i:=2; ;i+=3 { // Loop until we reach 100% confidence in x's integral-ness.
		if (f/i - f) < 1e-5 {
			return true; // If |f| - |f/i| is within 1e-5 of 0, return true immediately.
		} else if i%2 == 1 && f*float64((n + 1)/(2*i)) >= x { // Check whether i^2 has a chance of approximating x.
			f = float64((x / i) * (i / n));
		}
	}
}
