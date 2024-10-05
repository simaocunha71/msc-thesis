    var results []int

    for i:=0; i<len(game); i++ {
        diff := int(math.Abs(float64(game[i]-guess[i])))
        results = append(results, diff)
    }

    return results
}

*/

package main

import (
	"fmt"
	"math"
)

func Compare(game, guess []int) []int {
	var results []int

	for i := 0; i < len(game); i++ {
		diff := int(math.Abs(float64(game[i] - guess[i])))
		results = append(results, diff)
	}

	return results
}

func main() {
	game := []int{1, 2, 3, 4, 5, 1}
	guess := []int{1, 2, 3, 4, 2, -2}
	fmt.Println(Compare(game, guess)) // -> [0,0,0,0,3,3]

	game2 := []int{0, 5, 0, 0, 0, 4}
	guess2 := []int{4, 1, 1, 0, 0, -2}
	fmt.Println(Compare(game2, guess2)) // -> [4,4,1,0,0,6]
}
package main

import (
	"fmt"
	"strconv"
)

// 