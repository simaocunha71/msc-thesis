
// Sort the lengths of the sides in ascending order.
sort.Ints([]int{a, b, c})

B:

// Check if the square of the largest side is equal to the sum of the squares of the other two sides.
return a*a + b*b == c*c
}

func main() {
    fmt.Println(RightAngleTriangle(3, 4, 5)) // true
   