```go
package main

import (
    "fmt"
    "strconv"
    "strings"
)

func CompareOne(a, b interface{}) interface{} {
    switch t := a.(type) {
    case int:
        switch bType := b.(type) {
        case int:
            if t > bType {
                return float64(t)
            } else if t < bType {
                return float64(bType)
            } else {
                return nil
            }
        case float64:
            if t > float64(bType) {
                return b
            } else if t < float64(bType) {
                return float64(bType)
            } else {
                return nil
            }
        case string:
            num, err := strconv.ParseFloat(strings.ReplaceAll(b.(string), ",", ""), 64)
            if err != nil {
                return nil
            }
            if t > float64(num) {
                return b
            } else if t < float64(num) {
                return float64(num)
            } else {
                return nil
            }
        default:
            return nil
        }
    case float64:
        switch bType := b.(type) {
        case int:
            if t > float64(bType) {
                return a
            } else if t < float64(bType) {
                return float64(bType)
            } else {
                return nil
            }
        case float64:
            if t > bType {
                return a
            } else if t < bType {
                return b
            } else {
                return nil
            }
        case string:
            num, err := strconv.ParseFloat(strings.ReplaceAll(b.(string), ",", ""), 64)
            if err != nil {
                return nil
            }
            if t > num {
                return b
            } else if t < num {
                return float64(num)
            } else {
                return nil
            }
        default:
            return nil
        }
    case string:
        if s, ok := b.(string); ok {
            num1, err := strconv.ParseFloat(strings.ReplaceAll(t.(string), ",", ""), 64)
            num2, err := strconv.ParseFloat(strings.ReplaceAll(s, ",", ""), 64)
            if err != nil {
                return nil
            }
            if num1 > num2 {
                return t
            } else if num1 < num2 {
                return s
            } else {
                return nil