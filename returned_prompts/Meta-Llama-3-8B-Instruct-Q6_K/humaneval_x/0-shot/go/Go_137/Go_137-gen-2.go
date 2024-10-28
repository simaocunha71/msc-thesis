Here is the solution in Go:
```go
package main

import (
    "fmt"
    "strconv"
    "strings"
)

func CompareOne(a, b interface{}) interface{} {
    switch v := a.(type) {
    case int:
        switch w := b.(type) {
        case int:
            if v > w {
                return float64(v)
            } else if v < w {
                return float64(w)
            } else {
                return nil
            }
        case float64:
            if v > float64(w) {
                return float64(v)
            } else if v < float64(w) {
                return float64(w)
            } else {
                return nil
            }
        case string:
            s, err := strconv.ParseFloat(strings.ReplaceAll(w, ",", "."), 64)
            if err != nil {
                return w
            }
            if v > float64(s) {
                return w
            } else if v < float64(s) {
                return a
            } else {
                return nil
            }
        default:
            return a
    }
    case float64:
        switch w := b.(type) {
        case int:
            if v > float64(w) {
                return v
            } else if v < float64(w) {
                return w
            } else {
                return nil
            }
        case float64:
            if v > w {
                return v
            } else if v < w {
                return w
            } else {
                return nil
            }
        case string:
            s, err := strconv.ParseFloat(strings.ReplaceAll(w, ",", "."), 64)
            if err != nil {
                return w
            }
            if v > s {
                return w
            } else if v < s {
                return a
            } else {
                return nil
            }
        default:
            return a
    }
    case string:
        s, err := strconv.ParseFloat(strings.ReplaceAll(v, ",", "."), 64)
        if err != nil {
            return v
        }
        switch w := b.(type) {
        case int:
            s2, err := strconv.ParseFloat(strings.ReplaceAll(strconv.Itoa(w), ",", "."), 64)
            if err != nil {
                return w
            }
            if s > s2 {
                return v
            } else if s < s2 {
                return w
            } else {
                return