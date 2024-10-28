
// Return true is list elements are Strictly monotonically increasing or decreasing.
// >>> StrictlyMonotonic([1, 2, 4, 20])
// false
// >>> StrictlyMonotonic([1, 20, 4, 10])
// true
// >>> StrictlyMonotonic([4, 1, 0, -10])
// false
func StrictlyMonotonic(l []int) bool {

B:

// Return true is list elements are Strictly monotonically increasing.
// >>> StrictlyIncreasing([1, 2, 4, 20])
// false
// >>> StrictlyIncreasing([1, 20, 4, 10])
// false
// >>> StrictlyIncreasing([4, 1, 0, -10])
// true
func StrictlyIncreasing(l []int) bool {

C:

// Return true is list elements are Strictly monotonically decreasing.
// >>> StrictlyDecreasing([1, 2, 4, 20])
// true
// >>> StrictlyDecreasing([1, 20, 4, 10])
// false
// >>> StrictlyDecreasing([4, 1, 0, -10])
// false
func StrictlyDecreasing(l []int) bool {

D:

// Return true is list elements are Increasing.
// >>> Increasing([1, 2, 4, 20])
// true
// >>> Increasing([1, 20, 4, 10])
// false
// >>> Increasing([4, 1, 0, -10])
// true
func Increasing(l []int) bool {

E:

// Return true is list elements are Decreasing.
// >>> Decreasing([1, 2, 4, 20])
// false
// >>> Decreasing([1, 20, 4, 10])
// true
// >>> Decreasing([4, 1, 0, -10])