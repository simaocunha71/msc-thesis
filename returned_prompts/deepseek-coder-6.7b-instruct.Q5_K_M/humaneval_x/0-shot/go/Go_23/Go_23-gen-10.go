
return len(str)
}

// 
// Testing
// 

func main() {

fmt.Println(Strlen("")) // 0
fmt.Println(Strlen("abc")) // 3
}

*/

package main

import (
	"fmt"
)

func Strlen(str string) int {
	return len(str)
}

func main() {
	fmt.Println(Strlen(""))    // 0
	fmt.Println(Strlen("abc")) // 3
}
package main

import (
	"fmt"
)

// 