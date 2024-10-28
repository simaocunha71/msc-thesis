    var result string
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return strings.TrimSpace(result)
}

*/

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func StringSequence(n int) string {
	var result string
	for i := 0; i <= n; i++ {
		result += strconv.Itoa(i) + " "
	}
	return strings.TrimSpace(result)
}

func main() {
	fmt.Println(StringSequence(0))
	fmt.Println(StringSequence(5))
}

// Output
// 0
// 0 1 2 3 4 5

/*
The function "StringSequence" accepts an integer "n" as an input and returns a string containing space-delimited numbers starting from 0 upto n inclusive.
*/

/*
The function works by iterating over the range of numbers from 0 to n, converting each number to a string using the "strconv.Itoa" function, and appending it to the "result" string along with a space.

Finally, the function returns the "result" string, after removing any trailing spaces using the "strings.TrimSpace" function.
*/

/*
The main function calls the "StringSequence" function with different inputs and prints the returned string.
*/

/*
The output of the main function is the string representation of the numbers 0 through 5, separated by spaces.
*/
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"time"
)

type Response struct {
	Status string `json:"status"`
}

func main() {
	url := "http://localhost:8080/healthcheck"
	for {
		resp, err := http.Get(url)
		if err != nil {
			log.Printf("Failed to get healthcheck: %v\n", err)
			