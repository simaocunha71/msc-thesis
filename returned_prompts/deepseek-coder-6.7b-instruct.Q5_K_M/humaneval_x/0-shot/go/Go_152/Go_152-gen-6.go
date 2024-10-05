
	result := make([]int,len(game))

	for i := range game {
		result[i] = int(math.Abs(float64(game[i]-guess[i])))
	}

	return result
}


*/

package main

import (
	"fmt"
	"math"
)

func Compare(game, guess []int) []int {

	result := make([]int, len(game))

	for i := range game {
		result[i] = int(math.Abs(float64(game[i] - guess[i])))
	}

	return result
}

func main() {

	game := []int{1, 2, 3, 4, 5, 1}
	guess := []int{1, 2, 3, 4, 2, -2}

	fmt.Println(Compare(game, guess)) // Expected output: [0,0,0,0,3,3]

	game = []int{0, 5, 0, 0, 0, 4}
	guess = []int{4, 1, 1, 0, 0, -2}

	fmt.Println(Compare(game, guess)) // Expected output: [4,4,1,0,0,6]
}
package main

import (
	"fmt"
	"math"
)

func Compare(game, guess []int) []int {

	result := make([]int, len(game))

	for i := range game {
		result[i] = int(math.Abs(float64(game[i] - guess[i])))
	}

	return result
}

func main() {

	game := []int{1, 2, 3, 4, 5, 1}
	guess := []int{1, 2, 3, 4, 2, -2}

	fmt.Println(Compare(game, guess)) // Expected output: [0,0,0,0,3,