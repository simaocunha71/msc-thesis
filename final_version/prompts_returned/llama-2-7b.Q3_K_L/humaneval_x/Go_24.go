
// For a given number n, find the largest number that divides n evenly, smaller than n
// >>> LargestDivisor(15)
// 5
func LargestDivisor(n int) int {
	var largestDivisor = 0
	for _, divisors := range divideAndConquer(n) {
		largestDivisor = max(largestDivisor, largestDivisorFromList(divisors))
	}
	return largestDivisor + 1
}

func divideAndConquer(n int) []int {
	var result []int
	if n == 0 || n <= 2 {
		result = nil
		return result
	} else if n%2 == 0 {
		result = append([]int{2}, divideAndConquer(n/2)...)
		return result
	} else {
		result = append([]int{1,3}, divideAndConquer(n-1)...)
		return result
	}
}

func largestDivisorFromList(list []int) int {
	if len(list) == 0 {
		return -1
	} else if list[len(list)-1] > n {
		return -1
	} else if list[len(list)-1] == n {
		return largestDivisorFromList(list[:len(list)-1]) + 1
	} else {
		return list[len(list) - 2]
	}
}
