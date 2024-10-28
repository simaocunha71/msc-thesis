// Write your code here.
// [input] array.integer interval1
// An interval = (start, end) = (1, 2), where start is less or equal to end.
// 
// [input] array.integer interval2
// An interval = (start, end) = (1, 2), where start is less or equal to end.
// 
// [output] a string
// The length of the intersection of the two intervals, or "NO", if the two
// intervals don't intersect.
// 
// [note]
// A prime number is a natural number greater than 1 that has no positive divisors
// other than 1 and itself.
// See the Sample Tests for more information.
}

func main() {
	fmt.Println(Intersection([2]int{-3, -1}, [2]int{-5, 5})) //==> "YES"
	fmt.Println(Intersection([2]int{-1, 1}, [2]int{0, 4})) //==> "NO"
	fmt.Println(Intersection([2]int{1, 2}, [2]int{2, 3})) //==> "NO"
}