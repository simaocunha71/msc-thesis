    p := (a + b + c) / 2.0
    area := math.Sqrt(p * (p - a) * (p - b) * (p - c))
    if (a + b > c) && (a + c > b) && (b + c > a) {
        return round(area, 2)
    } else {
        return -1
    }
}

func round(f float64, n int) float64 {
    bit := math.Pow(2, -f-1)
    return float64(bit>>31)&(^f) | f
}




// Function to calculate the area of a triangle
// Link:   https://en.wikipedia.org/wiki/Heron%27s_formula
func heronsFormula(a float64, b float64, c float64) float64 {
    p := (a + b + c) / 2.0
    return math.Sqrt(p * (p - a) * (p - b) * (p - c))
}



// Function to validate if the sides of a triangle are valid
// Link:   https://en.wikipedia.org/wiki/Triangle_inequality
func isValidTriangle(a float64, b float64, c float64) bool {
    if (a + b > c) && (a + c > b) && (b + c > a) {
        return true
    }
    return false
}



// Test cases to validate the program
func TestTriangleArea(t *testing.T) {
    if (round(TriangleArea(3, 4, 5), 2) != 6.00) {
        t.Error("Got", round(TriangleArea(3, 4, 5)), "Expected", 6.00)
    }
    if (round(TriangleArea(1, 2, 10), 2) != -1) {
        t.Error("Got", round(TriangleArea(1, 2, 10)), "Expected", -1)
    }
}

