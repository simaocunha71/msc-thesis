
	sum := 0

B:

	for i := 2; i <= n; i += 2 {
		sum += i
		if sum == n {
			return true
		} else if sum > n {
			return false
		}
	}
	return false
}

// IsEqualToSumEven(4) => false
// IsEqualToSumEven(6) => false
// IsEqualToSumEven(8) => true
// IsEqualToSumEven(12) => false
// IsEqualToSumEven(14) => false
// IsEqualToSumEven(16) => true
// IsEqualToSumEven(18) => false
// IsEqualToSumEven(20) => false
// IsEqualToSumEven(22) => false
// IsEqualToSumEven(24) => true

// IsEqualToSumEven(26) => false
// IsEqualToSumEven(28) => false
// IsEqualToSumEven(30) => false
// IsEqualToSumEven(32) => true
// IsEqualToSumEven(34) => false
// IsEqualToSumEven(36) => false
// IsEqualToSumEven(38) => false
// IsEqualToSumEven(40) => false
// IsEqualToSumEven(42) => false
// IsEqualToSumEven(44) => true

// IsEqualToSumEven(46) => false
// IsEqualToSumEven(48) => false
// IsEqualToSumEven(50) => false
// IsEqualToSumEven(52) => false
// IsEqualToSumEven(54) => true
// IsEqualToSumEven(56) => false
// IsEqualToSumEven(58) => false
// IsEqualToSumEven(60) => false
// IsEqualToSumEven(62) => false
// IsEqualToSumEven(64) => true

// IsEqualToSumEven(66) => false
// IsEqualToSumEven(68) => false
// IsEqualToSumEven(70) => false
// IsEqualToSumEven(72) => false
// Is