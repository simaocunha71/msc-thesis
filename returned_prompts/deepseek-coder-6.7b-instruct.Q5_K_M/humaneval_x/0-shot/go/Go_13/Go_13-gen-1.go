    if a == 0 {
        return b
    }
    if b == 0 {
        return a
    }
    if a == b {
        return a
    }
    if a > b {
        return GreatestCommonDivisor(a % b, b)
    }
    return GreatestCommonDivisor(a, b % a)
}

func main() {

    fmt.Println(GreatestCommonDivisor(3, 5)) // Expected 1
    fmt.Println(GreatestCommonDivisor(25, 15)) // Expected 5
}


```


## 3.2.2. 유클리드 호제법 수정안

위의 코드에서 수정을 하였다. 그 이유는 마지막 두 return문이 순서를 바꾸었다. 그리고 재귀함수를 호출하기 전에 조건을 체크하는 것을 추가했다.

수정된 코드는 다음과 같다.

```go
package main

import "fmt"

// Return a greatest common divisor of two integers a and b
func GreatestCommonDivisor(a int,b int) int{
    if a == 0 {
        return b
    }
    if b == 0 {
        return a
    }
    if a == b {
        return a
    }
    if a > b {
        return GreatestCommonDiv