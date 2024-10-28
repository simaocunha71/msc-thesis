```go
package main

import (
    "fmt"
    "strconv"
    "strings"
)

func CompareOne(a, b interface{}) interface{} {
    // Convert a and b to their respective types
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
            if v > strconv.FormatFloat(w, 'f', -1, 64) {
                return v
            } else if v < strconv.FormatFloat(w, 'f', -1, 64) {
                return b
            } else {
                return nil
            }
        }
    case float64:
        switch w := b.(type) {
        case int:
            if v > float64(w) {
                return v
            } else if v < float64(w) {
                return float64(w)
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
            if v > strconv.ParseFloat(w, 64) {
                return v
            } else if v < strconv.ParseFloat(w, 64) {
                return b
            } else {
                return nil
            }
        }
    case string:
        switch w := b.(type) {
        case int:
            bFloat, err := strconv.ParseFloat(b.(interface{}.)(string), 64)
            if err != nil {
                return nil
            }
            if v > bFloat {
                return v
            } else if v < bFloat {
                return b
            } else {
                return nil
            }
        case float64:
            bFloat := float64(w)
            if v > strconv.FormatFloat(bFloat, 'f', -1, 64) {
                return v
            } else if v < strconv.FormatFloat(bFloat, 'f', -1, 64) {
                return b
            } else {
