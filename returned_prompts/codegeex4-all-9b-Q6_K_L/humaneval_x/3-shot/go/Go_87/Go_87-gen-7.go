
You have a logic error in your code. You are using the following condition to append the coordinates to the result slice:
if value == x {

This means that you are only appending coordinates where the value is exactly x. However, the problem statement is asking for the coordinates of any integer x in the list, not just the value of x.
To fix this, you should change the condition to:
if value >= x && value <= x+1 {

This will append the coordinates of any integer x in the list, regardless of its value.
Here's the corrected code:
func GetRow(lst [][]int, x int) [][2]int {
    result := make([][2]int, 0)
    for row, cols := range lst {
        for col, value := range cols {
            if value >= x && value <= x+1 {
                result = append(result, [2]int{row, col})
            }
        }
    }
    sort.Slice(result, func(i, j int) bool {
        if result[i][0] == result[j][0] {
            return result[i][1] > result[j][1]
        }
        return result[i][0] < result[j][0]
    })
    return result
}