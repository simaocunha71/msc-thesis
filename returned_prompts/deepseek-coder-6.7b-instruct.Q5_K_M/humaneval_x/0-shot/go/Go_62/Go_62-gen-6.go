
// Here we go through the array and for each element we multiply its index by the element.
// For the first element (xs[0]) we do not multiply as its index is 0 and derivative of any constant is 0.
// We start from index 1 as we have already handled the first element.
for i:= 1; i< len(xs); i++{
xs[i] = xs[i] * i
}

// After loop we start from index 1 (as we have already handled the first element)
return xs[1:]
}


*/

package main

import (
	"fmt"
)

func Derivative(xs []int) []int {
	for i := 1; i < len(xs); i++ {
		xs[i] = xs[i] * i
	}
	return xs[1:]
}

func main() {
	fmt.Println(Derivative([]int{3, 1, 2, 4, 5})) // [1, 4, 12, 20]
	fmt.Println(Derivative([]int{1, 2, 3}))        // [2, 6]
}
package main

import (
	"fmt"
)

type Node struct {
	val  int
	next *Node
}

func rotateRight(head *Node, k int) *Node {
	if head == nil || head.next == nil || k == 0 {
		return head
	}

	tail := head
	length := 1

	for tail.next != nil {
		tail = tail.next
		length++
	}

	tail.next = head
	k = k % length
	end := length - k

	for end > 0 {
		tail = tail.next
		end--
	}

	newHead := tail.next
	tail.next = nil

	return newHead
}

func printList(head *Node) {
	current := head
	for current != nil {
		fmt.Print(current.val, " ")
		current = current.next
	}