    if x == 0 {
        return "0"
    }

B:
    result := ""
    for x > 0 {
        result = strconv.Itoa(x % base) + result
        x /= base
    }
    return result
}

func main() {
    fmt.Println(ChangeBase(8, 3))
    fmt.Println(ChangeBase(8, 2))
    fmt.Println(ChangeBase(7, 2))
}
*/

package main

import (
	"fmt"
	"strconv"
)

func changeBase(x int, base int) string {
	if x == 0 {
		return "0"
	}

	result := ""
	for x > 0 {
		result = strconv.Itoa(x%base) + result
		x /= base
	}
	return result
}

func main() {
	fmt.Println(changeBase(8, 3))
	fmt.Println(changeBase(8, 2))
	fmt.Println(changeBase(7, 2))
}
package main

import (
	"fmt"
	"math"
)

// 