// The idea is to sort the sides in increasing order. If the sides are of
// lengths a, b, c, and if c is the largest among a, b, c, then
// a^2 + b^2 = c^2 is true for a right angle triangle.
// So, we sort the sides in increasing order and check the above condition.
func RightAngleTriangle(a, b, c int) bool {
	sides := []int{a, b, c}
	sort.Ints(sides)
	return sides[0]*sides[0]+sides[1]*sides[1] == sides[2]*sides[2]
}