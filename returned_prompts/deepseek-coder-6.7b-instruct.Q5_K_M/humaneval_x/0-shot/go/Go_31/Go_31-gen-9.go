
// Write your code here.

}

*/

package main

import "fmt"

func IsPrime(n int) bool {
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
	fmt.Println(IsPrime(6))
	fmt.Println(IsPrime(101))
	fmt.Println(IsPrime(11))
	fmt.Println(IsPrime(13441))
	fmt.Println(IsPrime(61))
	fmt.Println(IsPrime(4))
	fmt.Println(IsPrime(1))
}
package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func main() {
	wg.Add(2)

	go f1()
	go f2()

	wg.Wait()
}

func f1() {
	for i := 0; i < 10; i++ {
		fmt.Println("f1:", i)
	}
	wg.Done()
}

func f2() {
	for i := 0; i < 10; i++ {
		fmt.Println("f2:", i)
	}
	wg.Done()
}

// WaitGroup is used to wait for a collection of Goroutines to finish executing.
// The main goroutine calls Add to set the number of Goroutines to wait for.
// Then each of the Goroutines runs and calls wg.Done when finished.
// At the same time, wg.Wait can be used to block until all Goroutines have finished.
//
// This pattern is also useful to implement cancellation, timeout, or other forms of
// handling “work” in Go, as the work can be broken into multiple goroutines and
// the WaitGroup can be used to coordinate the starting and finishing of each.
//
// The code in main will