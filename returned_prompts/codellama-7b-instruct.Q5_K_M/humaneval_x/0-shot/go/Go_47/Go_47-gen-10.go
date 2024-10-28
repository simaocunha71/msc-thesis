	sort.Ints(l)
	var n = len(l)
	var m = n / 2
	if n%2 == 0 {
		return float64(l[m])
	}
	return float64(l[m-1] + l[m]) / 2
}

// Return Median of elements in the list l.
// >>> Median([3, 1, 2, 4, 5])
// 3.0
// >>> Median([-10, 4, 6, 1000, 10, 20])
// 15.0
func Median(l []float64) float64 {

B:
	sort.Float64s(l)
	var n = len(l)
	var m = n / 2
	if n%2 == 0 {
		return l[m]
	}
	return (l[m-1] + l[m]) / 2
}

// Return Median of elements in the list l.
// >>> Median([3, 1, 2, 4, 5])
// 3.0
// >>> Median([-10, 4, 6, 1000, 10, 20])
// 15.0
func Median(l []int64) float64 {

C:
	sort.Ints(l)
	var n = len(l)
	var m = n / 2
	if n%2 == 0 {
		return float64(l[m])
	}
	return float64(l[m-1] + l[m]) / 2
}

// Return Median of elements in the list l.
// >>> Median([3, 1, 2, 4, 5])
// 3.0
// >>> Median([-10, 4, 6, 1000, 10, 20])
// 15.0
func Median(l []uint64) float64 {

D:
	sort.Uints(l