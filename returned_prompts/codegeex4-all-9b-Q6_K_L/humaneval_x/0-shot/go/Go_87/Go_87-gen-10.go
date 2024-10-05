```go
import (
	"fmt"
)

func main() {
	lst := [][]int{
		{1, 2, 3, 4, 5, 6},
		{1, 2, 3, 4, 1, 6},
		{1, 2, 3, 4, 5, 1},
	}
	x := 1
	fmt.Println(GetRow(lst, x)) // Output: [[0 0] [1 4] [1 0] [2 5] [2 0]]
}

func GetRow(lst [][]int, x int) [][2]int {
	var result [][2]int

	for i, row := range lst {
		for j, num := range row {
			if num == x {
				result = append(result, [2]int{i, j})
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
```
The above code implements the function `GetRow` which takes a 2-dimensional list `lst` and an integer `x` as input, and returns a list of tuples representing the coordinates of all occurrences of `x` in the list. The coordinates are sorted first by row in ascending order, and then by column in descending order.

The code iterates over each element in the list and checks if it is equal to `x`. If it is, the coordinates of that element are added to the result list. After the iteration is complete, the result list is sorted using the `sort.Slice` function. The sorting function first checks if the rows of the two coordinates are the same. If they are, it compares the columns in descending order. If the rows are different, it compares the rows in ascending order.

The `main` function demonstrates how to use the `GetRow` function with a sample input and prints the output.