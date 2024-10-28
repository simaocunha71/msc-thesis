  for _, row := range grid {
    for _, cell := range row {
      if cell == 1 {
        goto B
      }
    }
  }
  return 0

B:
  steps := 0
  for _, row := range grid {
    for _, cell := range row {
      if cell == 1 {
        steps += int(math.Ceil(float64(cell) / float64(capacity)))
      }
    }
  }
  return steps
}


A: If there are no wells in the grid (all zeros), return 0.
B: If there are wells in the grid (at least one one), calculate the number of steps needed to empty all the wells.
This is done by dividing the total volume of the well by the bucket's capacity and rounding up to the nearest whole number. This is because you can only empty a bucket in integer amounts.

The time complexity of this solution is O(m*n) where m and n are the dimensions of the grid. This is because we must visit each cell in the grid once.
The space complexity of this solution is O(1) because we only use a constant amount of space to store the variables steps and capacity.
*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(MaxFill([][]int{{0, 0, 1, 0}, {0, 1, 0, 0}, {1, 1, 1, 1}}, 1)) // 6
	fmt.Println(MaxFill([][]int{{0, 0, 1, 1}, {0, 0, 0, 0}, {1, 1, 1, 1}, {0, 1, 1, 1}}, 2)) // 5
	fmt.Println(MaxFill([][]int{{0, 0, 0}, {0, 0, 0}}, 5)) // 0
}
package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 4