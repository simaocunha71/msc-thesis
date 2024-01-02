
// Return true if all numbers in the list l are below threshold t.
// >>> BelowThreshold([1, 2, 4, 10], 100)
// true
// >>> BelowThreshold([1, 20, 4, 10], 5)
// false
func BelowThreshold(l []int,t int) bool {
    if len(l) == 0 {
        return true
    }
    maxi := maxInt(l)
    if (maxi < t || maxi-t <= 1) {
        return false
    } else {
        return BelowThreshold(l[1:], t - l[0])
    }
}
