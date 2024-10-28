func TriangleArea(a float64, b float64, c float64) float64 {
	if a+b <= c || a+c <= b || b+c <= a {
		return -1
	}
	s := (a + b + c) / 2
	area := math.Sqrt(s * (s - a) * (s - b) * (s - c))
	return math.Round(area*100)/100
}
func main() {
	fmt.Println(TriangleArea(3, 4, 5)) // 6.00
	fmt.Println(TriangleArea(1, 2, 10)) // -1
}