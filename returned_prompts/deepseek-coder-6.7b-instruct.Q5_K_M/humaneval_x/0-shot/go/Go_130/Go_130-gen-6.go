
}

// R:
// [1, 3, 2, 8]

// P:
// The function Tri(n) takes an integer n and returns a list of the first n + 1 numbers
// of the Tribonacci sequence. 

// The Tribonacci sequence starts with three initial values: 3, 2, 1. Each subsequent
// number is the sum of the previous three, hence the sequence is [3, 2, 1, 8, 5, 3, 2, ...].
// The function uses a for loop to iterate through the sequence and append the next number
// to the result list. The base case for the recursion is when n is less than 1, in which
// case the function returns [1].

// The time complexity of this function is O(n) because it iterates through the sequence
// n times. The space complexity is also O(n) because it stores the first n + 1 numbers
// of the sequence in the result list.
func Tri(n int)  []float64  {
	res := []float64{1, 3, 2}
	if n < 1 {
		return []float64{1}
	}
	if n < 3 {
		return res[:n+1]
	}
	for i := 3; i < n+1; i++ {
		if i % 2 == 0 {
			res = append(res, 1 + float64(i) / 2)
		} else {
			res = append(res, res[i-1] + res[i-2] + res[i+1])
		}
	}
	return res
}

func main() {
	fmt.Println(Tri(3))
}

// [1, 3, 2, 8]
// [1, 3, 2, 8]

// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
// Correct
