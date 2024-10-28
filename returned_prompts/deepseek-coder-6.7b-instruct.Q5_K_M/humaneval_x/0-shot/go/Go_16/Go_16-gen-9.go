    str = strings.ToLower(str)
    count := 0
    m := make(map[rune]bool)

    for _, ch := range str {
        if _, ok := m[ch]; !ok {
            m[ch] = true
            count++
        }
    }

    return count
}

*/

package main

import (
	"fmt"
	"strings"
)

func CountDistinctCharacters(str string) int {
	str = strings.ToLower(str)
	count := 0
	m := make(map[rune]bool)

	for _, ch := range str {
		if _, ok := m[ch]; !ok {
			m[ch] = true
			count++
		}
	}

	return count
}

func main() {
	fmt.Println(CountDistinctCharacters("xyzXYZ")) // 3
	fmt.Println(CountDistinctCharacters("Jerry"))  // 4
}
package main

import (
	"fmt"
	"sync"
)

type (
	Fetcher interface {
		Fetch(url string) (body string, urls []string, err error)
	}

	SafeMap struct {
		mux  sync.Mutex
		urls map[string]bool
	}
)

func (sm *SafeMap) check(url string) bool {
	sm.mux.Lock()
	defer sm.mux.Unlock()
	if _, ok := sm.urls[url]; ok {
		return true
	}
	sm.urls[url] = true
	return false
}

func Crawl(url string, depth int, fetcher Fetcher, sm *SafeMap) {
	if depth <= 0 {
		return
	}
	if sm.check(url) {
		return
	}
	body, urls, err := fetcher.Fetch(url)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("found: %s %q\n", url,