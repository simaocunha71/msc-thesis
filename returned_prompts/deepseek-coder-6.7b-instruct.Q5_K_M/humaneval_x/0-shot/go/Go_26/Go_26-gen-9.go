
	result := make([]int, 0)
	occurrences := make(map[int]int)

	for _, number := range numbers {
		occurrences[number] += 1
	}

	for _, number := range numbers {
		if occurrences[number] == 1 {
			result = append(result, number)
		}
	}

	return result
}

*/

package main

import (
	"fmt"
)

func RemoveDuplicates(numbers []int) []int {
	result := make([]int, 0)
	occurrences := make(map[int]int)

	for _, number := range numbers {
		occurrences[number] += 1
	}

	for _, number := range numbers {
		if occurrences[number] == 1 {
			result = append(result, number)
		}
	}

	return result
}

func main() {
	numbers := []int{1, 2, 3, 2, 4}
	fmt.Println(RemoveDuplicates(numbers)) // [1, 3, 4]
}
package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Coordinate struct {
	x int
	y int
}

func main() {
	input, _ := os.ReadFile("input.txt")

	directions := map[string]Coordinate{
		"U": {0, 1},
		"D": {0, -1},
		"L": {-1, 0},
		"R": {1, 0},
	}

	lines := strings.Split(string(input), "\n")
	tailVisited := make(map[Coordinate]bool)

	head := Coordinate{0, 0}
	tail := Coordinate{0, 0}
	tailVisited[tail] = true

	for _, line := range lines {
		parts := strings.Split(line, " ")
		dir