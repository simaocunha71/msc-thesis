
func Fibfib(n int) int {
	if n < 2 {
		return 0
	}
	if n == 2 {
		return 1
	}

	a, b, c := 0, 0, 1
	for i := 3; i <= n; i++ {
		a, b, c = b, c, a+b+c
	}
	return c
}

// Fibfib(1) 의 경우 0
// Fibfib(5) 의 경우 4
// Fibfib(8) 의 경우 24

해당 문제는 동적 계획법을 이용한 문제로, 점화식을 구현하면 된다.
초기 값은 Fibfib(0)은 0, Fibfib(1)은 0, Fibfib(2)는 1로 설정한다.
그리고 반복문을 이용해서 Fibfib(n)을 구하면 된다.

이 방법을 이용하면 시간 복잡도는 O(n)이 된다.

*/

package main

import "fmt"

func Fibfib(n int) int {
	if n < 2 {
		return 0
	}
	if n == 2 {
		return 1
	}

	a, b, c := 0, 0, 1
	for i := 3;