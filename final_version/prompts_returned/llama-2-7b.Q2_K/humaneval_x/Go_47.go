import (
	"sort"
)

// Return Median of elements in the list l.
// >>> Median([3, 1, 2, 4, 5])
// 3.0
// >>> Median([-10, 4, 6, 1000, 10, 20])
// 15.0
func Median(l []int) float64 {
	n := len(l)
	if n == 0 || n == 1 {
		return float64(n == 1) ? l[0] : 0.0
	}
	f := float64(len(l)) / 2
	switch {
	case n > 3:
		l = append(l[:0:3], l...)
		l = append(l[:0:1], l...)...
	case f >= n/4:
		l = append(l[:f*2-1], l[f*2:]...)
	}

	if sort.IsSorted(l) {
		var p float64
		switch {
		case n > 3 && f >= n/8:
			p = (n - 3 + 1)/2.0
		default:
			p = f
		}
		return sum(l[:p]) / float64(p)
	} else {
		var lp [][]int
		lp[0] = make([]int, n/2-1)
		for i := range lp {
			lp[i] = l[i:(len(l)/2)+i+n%2+i:3*n/2]...
		}
		return Sum(lp...)...
	}
}
