
I'm not sure what you are asking.  Your code is correct for the first two problems.
For the third problem, you are making a floating point comparison, which is a common problem in programming.  If the difference is small enough, you should consider it equal.  For example, if the difference is less than 0.000001, you should consider it equal.  You can use the math.Abs function to get the absolute value of the difference, and then compare it to your threshold.
Here is a corrected version of your code:
func Compare(game, guess []int) []int {
    result := make([]int, 0)
    for i := 0; i < len(game); i++ {
        diff := math.Abs(float64(game[i]) - float64(guess[i]))
        if diff < 0.000001 {
            result = append(result, 0)
        } else {
            result = append(result, int(diff))
        }
    }
    return result
}