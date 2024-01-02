import (
    "strconv"
)

// Write a function that takes an array of numbers as input and returns
// the number of elements in the array that are greater than 10 and both
// first and last digits of a number are odd (1, 3, 5, 7, 9).
// For example:
// Specialfilter([15, -73, 14, -15]) => 1
// Specialfilter([33, -2, -3, 45, 21, 109]) => 2
func Specialfilter(nums []int) int {
    var n = len(nums)
    if n == 0 {
        return 0
    } else {
        for i := 0; i < n && nums[i] > 10; i++ { // i+1
            if !(nums[i]%2 == 1 || nums[i-1]%2 == 1) {
                return n - i + 1 //i-1 is in the range of [0,n-1], but nums in this list.
            }
        }
    }
    return 0
}

// Input: [15, -73, 14, -15] Output: 1 Explanation: The first four elements satisfy the condition: [15, -73, 14, -15], but the last one does not.
func main() {
    var input = []int{15, -73, 14, -15}
    fmt.Println(Specialfilter(input))
}
