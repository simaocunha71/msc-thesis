    if (a + b > c) && (b + c > a) && (c + a > b) {
        // calculate semi-perimeter
        s := (a + b + c) / 2

        // calculate area using Heron's formula
        area := math.Sqrt(s * (s - a) * (s - b) * (s - c))

        return math.Round(area*100) / 100
    } else {
        return -1
    }
}
*/

// import (
// 	"testing"
// )

// func TestTriangleArea(t *testing.T) {
// 	type test struct {
// 		a, b, c float64
// 		want     float64
// 	}

// 	tests := []test{
// 		{3, 4, 5, 6},
// 		{1, 2, 10, -1},
// 	}

// 	for _, tc := range tests {
// 		got := TriangleArea(tc.a, tc.b, tc.c)
// 		if got != tc.want {
// 			t.Errorf("TriangleArea(%f, %f, %f): want %f, got %f", tc.a, tc.b, tc.c, tc.want, got)
// 		}
// 	}
// }

// func main() {
// 	fmt.Println(TriangleArea(3, 4, 5))
// 	fmt.Println(TriangleArea(1, 2, 10))
// }

import (
	"testing"
)

func TestTriangleArea(t *testing.T) {
	type test struct {
		a, b, c float64
		want    float64
	}

	tests := []test{
		{3, 4, 5, 6},
		{1, 2, 10, -1},
	}

	for _, tc := range tests {
		got := Tri