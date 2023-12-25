
// Return true is list elements are Monotonically increasing or decreasing.
// >>> Monotonic([1, 2, 4, 20])
// true
// >>> Monotonic([1, 20, 4, 10])
// false
// >>> Monotonic([4, 1, 0, -10])
// true
func Monotonic(l []int) bool {
	if len(l) == 0 {
		return true
	}
	switch x := l[0]; {
	case x < 0:
		fallthrough
	case x > math.MaxInt64-1:
		x = -math.MaxInt64 + x
	default:
		fallthrough
	case x == 0:
		return true
	}

	if x < l[0] {
		return false
	} else if x > l[len(l)-1] {
		for i, j := 2, len(l)-2; i < j; i = (i + 2) % j+1, j++ {
			if l[i]+l[j-1] == -math.MaxInt64+x || x > l[i]+l[j-1] {
				return false
			}
		}
	} else if x == 0 {
		for i := 0; (i < len(l)-2) && (l[i+1]+x > -math.MaxInt64); i++ {
			if x+l[i] <= l[j-1] {
				return false
			}
		}
	} else if x != 0 && ((math.MaxInt64-x) >= l[len(l)-2]+x || (x - (l[len(l)-2] + x)) <= -math.MaxInt64+l[0]) {
		return false
	}
	for i := 1; ; i++ {
		if l[i-1]*2 >= math.MaxUint32 || (math.MaxUint32/2)