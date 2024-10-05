
// Add two numbers x and y
// 5
// 12

// 2, 3
// 5
// 5, 7
// 12

}

// Testing
func main() {

B:

// Testing
// Add(2, 3) == 5
// Add(5, 7) == 12

}
```

## 4. ตัวอย่างโปรแกรมสำหรับการรับค่าจากผู้ใช้ทางคีย์บอร์ด

```go
package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "strings"
)

func Add(x int, y int) int {
    return x + y
}

func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter two numbers: ")
    text, _ := reader.ReadString('\n')
    numbers := strings.Fields(text)
    x, _ := strconv.Atoi(numbers[0])
    y, _ := strconv.Atoi(numbers[1])
    fmt.Println("Result:", Add(x, y))
}
```

ภายใต้การรับค่าจากผู้ใช้ทางคีย์บอร์ด เราจะใช้ `bufio` เพื่ออ่า