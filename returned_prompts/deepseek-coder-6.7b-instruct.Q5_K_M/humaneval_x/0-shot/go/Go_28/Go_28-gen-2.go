
// Concatenate list of strings into a single string
func Concatenate(strings []string) string {
    result := ""
    for _, str := range strings {
        result += str
    }
    return result
}

*/

package main

import "fmt"

// Concatenate list of strings into a single string
func Concatenate(strings []string) string {
	result := ""
	for _, str := range strings {
		result += str
	}
	return result
}

func main() {
	fmt.Println(Concatenate([]string{}))
	fmt.Println(Concatenate([]string{"a", "b", "c"}))
}
package main

import (
	"fmt"
	"sync"
)

// SafeCounter is safe to use concurrently.
type SafeCounter struct {
	mu sync.Mutex
	v  map[string]int
}

// Inc increments the counter for the given key.
func (c *SafeCounter) Inc(key string) {
	c.mu.Lock()
	// Lock so only one goroutine at a time can access the map c.v.
	c.v[key]++
	// Release the lock
	c.mu.Unlock()
}

// Value returns the current value of the counter for the given key.
func (c *SafeCounter) Value(key string) int {
	c.mu.Lock()
	// Lock so only one goroutine at a time can access the map c.v.
	defer c.mu.Unlock()
	return c.v[key]
}

func main() {
	c := SafeCounter{v: make(map[string]int)}
	for i := 0; i < 100; i++ {
		go c.Inc("somekey")
	}

	fmt.Println(c.Value("somekey"))
}

/*

Mutex is used to provide a way to synchronize access to shared state across multiple goroutines.

In this program, the Inc method (which increments the counter) and the Value method (which reads the current counter)