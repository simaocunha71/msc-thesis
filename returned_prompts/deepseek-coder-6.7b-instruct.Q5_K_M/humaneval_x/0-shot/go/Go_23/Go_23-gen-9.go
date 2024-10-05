
return len(str)

}

*/
package main

import (
	"fmt"
)

func Strlen(str string) int {
	return len(str)
}

func main() {
	fmt.Println(Strlen(""))
	fmt.Println(Strlen("abc"))
}
package main

import (
	"fmt"
	"math"
)

func IsPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	sqrt := int(math.Sqrt(float64(n)))
	for i := 3; i <= sqrt; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(IsPrime(2))
	fmt.Println(IsPrime(1))
	fmt.Println(IsPrime(121))
	fmt.Println(IsPrime(101))
}

/*
