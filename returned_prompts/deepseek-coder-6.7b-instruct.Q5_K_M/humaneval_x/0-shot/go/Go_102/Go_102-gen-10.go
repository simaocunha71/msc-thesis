
// A loop will be created to go through the range from x to y
for i := x; i <= y; i++ {

B:

// If the number is even, then it will be returned and the loop will end
if i%2 == 0 {
  return i
}

C:

// If the end of the range has been reached and no even number has been found, then -1 will be returned
if i == y && i%2 != 0 {
  return -1
}

}

return -1

}

func main()  {
fmt.Println(ChooseNum(12, 15)) // 14
fmt.Println(ChooseNum(13, 12)) // -1
}

// The function works by iterating over the range from x to y and checks if the number is even.
// If it is, then it is returned. If the end of the range is reached and no even number was found, then -1 is returned.
// This function runs with a time complexity of O(n) as it iterates over the range once.
// The space complexity is constant, O(1), because it only uses a single integer variable to store the result and does not use any additional data structures.

// It's also worth mentioning that the provided solution assumes that x and y are always positive. If the function is to be used with negative numbers, additional checks would have to be added to handle them properly.

// Also, this function does not handle cases where y < x, as it is assumed that x and y are positive. If this function is to be used in such cases, additional error checking would have to be added.
































































































































