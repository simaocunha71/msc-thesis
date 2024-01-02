
// Given length of a side and high return area for a triangle.
// >>> TriangleArea(5, 3)
// 7.5
func TriangleArea(a float64, h float64) float64 {
	return math.Sqrt((a * (1 - math.Pow(float64(h), 2))) / 2)
}