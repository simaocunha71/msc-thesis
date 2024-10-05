
// Initialize a variable to store the count of the substring
  count := 0

// Loop through the string
  for i := 0; i < len(str) - len(substring) + 1; i++ {

// For each position, check if the substring matches the slice of the string from that position
    if str[i:i+len(substring)] == substring {

// If it does, increment the count
      count++
    }
  }

// Return the count
  return count
}

// Call the function with the provided test cases
fmt.Println(HowManyTimes("", "a")) // 0
fmt.Println(HowManyTimes("aaa", "a")) // 3
fmt.Println(HowManyTimes("aaaa", "aa")) // 3

// Output:
// 0
// 3
// 3
// Process finished with the exit code 0
*/

// Solution ends here.

package main

import (
	"fmt"
)

func HowManyTimes(str string, substring string) int {
	count := 0
	for i := 0; i < len(str)-len(substring)+1; i++ {
		if str[i:i+len(substring)] == substring {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(HowManyTimes("", "a"))    // 0
	fmt.Println(HowManyTimes("aaa", "a")) // 3
	fmt.Println(HowManyTimes("aaaa", "aa")) // 3
}
package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
)

type Movie struct {
	ID       string    `json:"id"`
	Isbn     string    `json:"isbn"`
	Title    string    `json:"title"`
	Director *Director `json:"director"`
}

type Director struct {
	FirstName string