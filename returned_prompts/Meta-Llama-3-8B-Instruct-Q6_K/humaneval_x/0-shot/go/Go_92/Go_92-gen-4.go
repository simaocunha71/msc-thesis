```go
package main

import (
    "fmt"
    "reflect"
)

func AnyInt(x, y, z interface{}) bool {
    if reflect.TypeOf(x).Kind() != reflect.Int && reflect.TypeOf(x).Kind() != reflect.Int8 && reflect.TypeOf(x).Kind() != reflect.Int16 && reflect.TypeOf(x).Kind() != reflect.Int32 && reflect.TypeOf(x).Kind() != reflect.Int64 {
        return false
    }
    if reflect.TypeOf(y).Kind() != reflect.Int && reflect.TypeOf(y).Kind() != reflect.Int8 && reflect.TypeOf(y).Kind() != reflect.Int16 && reflect.TypeOf(y).Kind() != reflect.Int32 && reflect.TypeOf(y).Kind() != reflect.Int64 {
        return false
    }
    if reflect.TypeOf(z).Kind() != reflect.Int && reflect.TypeOf(z).Kind() != reflect.Int8 && reflect.TypeOf(z).Kind() != reflect.Int16 && reflect.TypeOf(z).Kind() != reflect.Int32 && reflect.TypeOf(z).Kind() != reflect.Int64 {
        return false
    }
    if x.(int)+y.(int)+z.(int) == x.(int) {
        return true
    }
    if x.(int)+y.(int) == z.(int) {
        return true
    }
    if y.(int)+z.(int) == x.(int) {
        return true
    }
    return false
}

func main() {
    fmt.Println(AnyInt(5, 2, 7)) // true
    fmt.Println(AnyInt(3, 2, 2)) // false
    fmt.Println(AnyInt(3, -2, 1)) // true
    fmt.Println(AnyInt(3.6, -2.2, 2)) // false
}
```



The task is to create a function `AnyInt` that takes three numbers as input and returns `true` if one of the numbers is equal to the sum of the other two, and all numbers are integers. Otherwise, it returns `false`.

The function first checks if all the input numbers are integers using the `reflect` package. If any of the numbers is not an integer, the function returns `false`.

If all the numbers are integers, the function then checks if one of the numbers is equal to the sum of the other two. If such a condition is found, the function returns `true`. Otherwise, it returns `false`.

The examples provided show that the function should return