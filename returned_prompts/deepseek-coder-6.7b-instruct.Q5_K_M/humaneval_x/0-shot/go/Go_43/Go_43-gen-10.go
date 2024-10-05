
// M:

    // create a map to store the elements of the list
    m := make(map[int]bool)

B:

    // iterate over the list
    for _, num := range l {

C:

        // if the opposite of the current number is in the map, return true
        if _, ok := m[-num]; ok {
            return true
        }

D:

        // otherwise, add the current number to the map
        m[num] = true
    }

E:

    // if we get through the entire list without finding a pair that sums to zero, return false
    return false
}

*/

func PairsSumToZero(l []int) bool {
	m := make(map[int]bool)
	for _, num := range l {
		if _, ok := m[-num]; ok {
			return true
		}
		m[num] = true
	}
	return false
}

// this is a test
func main() {
	l := []int{2, 4, -5, 3, 5, 7}
	fmt.Println(PairsSumToZero(l))
}
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"time"
)

const (
	DefaultPort = "8080"
	DefaultUrl  = "http://localhost:8080"
)

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = DefaultPort
		log.Printf("Defaulting to port %s", port)
	}

	url := os.Getenv("URL")
	if url == "" {
		url = DefaultUrl
		log.Printf("Defaulting to url %s", url)
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		proxyRequest, err := http.NewRequest(r.Method, url, r.Body)
		if err != nil {
			