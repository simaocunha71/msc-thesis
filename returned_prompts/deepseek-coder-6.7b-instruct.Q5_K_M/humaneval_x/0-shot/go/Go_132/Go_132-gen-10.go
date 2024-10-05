
	n := len(s)
	stack := make([]rune, 0, n)

	for _, c := range s {
		if c == '[' {
			stack = append(stack, c)
		} else {
			if len(stack) == 0 {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) > 0
}

*/

package main

import (
	"fmt"
)

func IsNested(s string) bool {

	n := len(s)
	stack := make([]rune, 0, n)

	for _, c := range s {
		if c == '[' {
			stack = append(stack, c)
		} else {
			if len(stack) == 0 {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) > 0
}

func main() {
	fmt.Println(IsNested("[[]]"))                         // ➞ true
	fmt.Println(IsNested("[]]]]]]][[[[[]"))              // ➞ false
	fmt.Println(IsNested("[][]"))                         // ➞ false
	fmt.Println(IsNested("[]"))                           // ➞ false
	fmt.Println(IsNested("[[][]]"))                       // ➞ true
	fmt.Println(IsNested("[[]][["))                       // ➞ true
	fmt.Println(IsNested("[[[][]]][[]][][[[][]]][][[]][]")) // ➞ true
}
package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"
	"os/signal"
	"time"

	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()

	r.HandleFunc("/", func(w http.ResponseWriter