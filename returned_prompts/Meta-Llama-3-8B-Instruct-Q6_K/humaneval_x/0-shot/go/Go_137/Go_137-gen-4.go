```go
package main

import (
    "fmt"
    "strconv"
    "strings"
)

// Create a function that takes integers, floats, or strings representing
// real numbers, and returns the larger variable in its given variable type.
// Return nil if the values are equal.
// Note: If a real number is represented as a string, the floating point might be . or ,

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
                return v1
            } else if v1 < float64(v2) {
                return v2
            } else {
                return nil
            }
        case string:
            f, err := strconv.ParseFloat(v2, 64)
            if err != nil {
                return v2
            }
            if v1 > float64(f) {
                return v1
            } else if v1 < float64(f) {
                return v2
            } else {
                return nil
            }
        }
    case float64:
        switch v2 := b.(type) {
        case int:
            if v1 > float64(v2) {
                return v1
            } else if v1 < float64(v2) {
                return v2
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
            f, err := strconv.ParseFloat(v2, 64)
            if err != nil {
                return v2
            }
            if v1 > f {
                return v1
            } else if v1 < f {
                return v2
            } else {
                return nil
            }
        }
    case string:
        s1 := strings.ReplaceAll(v1, ".", "")
        s1 = strings.ReplaceAll(s1, ",", ".")
        f1, err := strconv.ParseFloat(s1, 64)
        if err != nil {
            return