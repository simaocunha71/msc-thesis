
// Given length of a side and high return area for a triangle.
// >>> TriangleArea(5, 3)
// 7.5
func TriangleArea(a float64, h float64) float64 {
	return 0.5 * (h / 2 - sqrt(double((b-a)/2 + h*sin(90))/((b-a)/2 + h*sin(90))))
}
