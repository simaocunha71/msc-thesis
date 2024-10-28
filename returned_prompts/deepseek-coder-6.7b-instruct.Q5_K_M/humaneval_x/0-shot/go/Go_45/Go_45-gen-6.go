
	area := (a * h) / 2

	return area
}


// Given length of a side and high return perimeter for a triangle.
// >>> TrianglePerimeter(5, 3)
// 11
func TrianglePerimeter(a float64, h float64) float64 {

P:

	perimeter := 2 * (a + h)

	return perimeter
}

// Given length of three sides return area for a triangle.
// >>> TriangleArea(3, 4, 5)
// 6
func TriangleAreaThreeSides(a float64, b float64, c float64) float64 {

	sp := (a + b + c) / 2
	area := math.Sqrt(sp * (sp-a) * (sp-b) * (sp-c))
	
	return area
}

// Given length of three sides return perimeter for a triangle.
// >>> TrianglePerimeter(3, 4, 5)
// 12
func TrianglePerimeterThreeSides(a float64, b float64, c float64) float64 {

	perimeter := a + b + c

	return perimeter
}

// Given length of two sides and angle between them return area for a triangle.
// >>> TriangleArea(3, 4, 60)
// 6
func TriangleAreaTwoSidesAngle(a float64, b float64, angle float64) float64 {

	angle = angle * (math.Pi / 180)
	area := (a * b * math.Sin(angle)) / 2

	return area
}

// Given length of two sides and angle between them return perimeter for a triangle.
// >>> TrianglePerimeter(3, 4, 60)
// 12
func TrianglePerimeterTwoSidesAngle(a float64, b float64, angle float64) float64 {

	angle = angle * (math.Pi / 180)
	c := math.Sqrt