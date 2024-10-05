    count := 0
    vowels := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'y': true}
    
    s = strings.ToLower(s)
    
    for _, c := range s {
        if _, ok := vowels[c]; ok {
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

func VowelsCount(s string) int {
	count := 0
	vowels := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'y': true}

	s = strings.ToLower(s)

	for _, c := range s {
		if _, ok := vowels[c]; ok {
			count++
		}
	}

	return count
}

func main() {
	fmt.Println(VowelsCount("abcde")) // 2
	fmt.Println(VowelsCount("ACEDY")) // 3
}
package main

import (
	"fmt"
)

type node struct {
	value int
	next  *node
}

type linkedList struct {
	head *node
	tail *node
}

func (l *linkedList) append(val int) {
	newNode := &node{
		value: val,
		next:  nil,
	}
	if l.head == nil {
		l.head = newNode
		l.tail = newNode
	} else {
		l.tail.next = newNode
		l.tail = newNode
	}
}

func (l *linkedList) display() {
	temp := l.head
	for temp != nil {
		fmt.Print(temp.value, " ")
		temp = temp.next
	}
	fmt.Println()
}

func (l *linkedList) reverse() {
	prev := &node{}
