
	n := len(s)
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

*/

package main

import "fmt"

func PrimeLength(s string) bool {

	n := len(s)
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(PrimeLength("Hello"))
	fmt.Println(PrimeLength("abcdcba"))
	fmt.Println(PrimeLength("kittens"))
	fmt.Println(PrimeLength("orange"))
}
package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()

	ch := make(chan int)

	go func() {
		time.Sleep(2 * time.Second)
		ch <- 1
	}()

	select {
	case val := <-ch:
		fmt.Println(val)
	case <-time.After(1 * time.Second):
		fmt.Println("Timeout")
	}

	elapsed := time.Since(start)
	fmt.Printf("Execution Time: %s\n", elapsed)
}
package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()

	ch := make(chan int)
	timeout := time.After(1 * time.Second)

	go func() {
		time.Sleep(2 * time.Second)
		ch <- 1
	}()

	select {
	case val := <-ch:
		fmt.Println(val)
	case <-timeout:
		fmt.Println("Timeout")
	}

	elapsed