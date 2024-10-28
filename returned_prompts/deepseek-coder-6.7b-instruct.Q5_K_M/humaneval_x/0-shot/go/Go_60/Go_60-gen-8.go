
    sum := 0
    for i := 1; i <= n; i++ {
        sum += i
    }
    return sum

}

*/

package main

import "fmt"

func SumToN(n int) int {
	sum := 0
	for i := 1; i <= n; i++ {
		sum += i
	}
	return sum
}

func main() {
	fmt.Println(SumToN(30))  // 465
	fmt.Println(SumToN(100)) // 5050
	fmt.Println(SumToN(5))   // 15
	fmt.Println(SumToN(10))  // 55
	fmt.Println(SumToN(1))   // 1
}
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"sync"
)

type Result struct {
	Id    int
	Title string
	Body  string
}

func main() {

	url := "https://jsonplaceholder.typicode.com/posts/1"
	wg := new(sync.WaitGroup)
	m := new(sync.Mutex)

	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			resp, err := http.Get(url)
			if err != nil {
				fmt.Println(err)
				return
			}
			defer resp.Body.Close()
			body, err := ioutil.ReadAll(resp.Body)
			if err != nil {
				fmt.Println(err)
				return
			}
			result := Result{}
			err = json.Unmarshal(body, &result)
			if err != nil {
				fmt.Println(err)
				return
			}
			m.Lock()
			fmt.Println(