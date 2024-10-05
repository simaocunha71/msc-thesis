Here is a possible solution to the problem:
```go
package main

import (
    "fmt"
    "strconv"
    "strings"
)

func CompareOne(a, b interface{}) interface{} {
    switch v1 := a.(type) {
    case int:
        switch v2 := b.(type) {
        case int:
            if v1 > v2 {
                return float64(v1)
            } else if v1 < v2 {
                return float64(v2)
            } else {
                return nil
            }
        case float64:
            if v1 > float64(v2) {
                return float64(v1)
            } else if v1 < float64(v2) {
                return float64(v2)
            } else {
                return nil
            }
        case string:
            num2, err := strconv.ParseFloat(v2, 64)
            if err != nil {
                return v2
            }
            if v1 > float64(num2) {
                return v1
            } else if v1 < float64(num2) {
                return v2
            } else {
                return nil
            }
        default:
            return nil
        }
    case float64:
        switch v2 := b.(type) {
        case int:
            if v1 > float64(v2) {
                return v1
            } else if v1 < float64(v2) {
                return float64(v2)
            } else {
                return nil
            }
        case float64:
            if v1 > v2 {
                return v1
            } else if v1 < v2 {
                return v2
            } else {
                return nil
            }
        case string:
            num2, err := strconv.ParseFloat(v2, 64)
            if err != nil {
                return v2
            }
            if v1 > num2 {
                return v1
            } else if v1 < num2 {
                return v2
            } else {
                return nil
            }
        default:
            return nil
        }
    case string:
        switch v2 := b.(type) {
        case int:
            num1, err := strconv.ParseFloat(v1, 64)
            if err != nil {
                return v1
            }
            if num1 > float64(v2) {
                return v1
            } else if num1 < float64(v2) {
               