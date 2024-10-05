```go
package main

import (
    "fmt"
    "strconv"
    "strings"
)

func CompareOne(a, b interface{}) interface{} {
    switch a.(type) {
    case int:
        switch b.(type) {
        case int:
            if a.(int) > b.(int) {
                return a
            } else if a.(int) < b.(int) {
                return b
            } else {
                return nil
            }
        case float64:
            if a.(int) > float64(b.(int)) {
                return a
            } else if a.(int) < float64(b.(int)) {
                return b
            } else {
                return nil
            }
        case string:
            if a.(int) > int(strconv.Atoi(strings.Replace(b.(string), ",", "", -1))) {
                return a
            } else if a.(int) < int(strconv.Atoi(strings.Replace(b.(string), ",", "", -1))) {
                return b
            } else {
                return nil
            }
        }
    case float64:
        switch b.(type) {
        case int:
            if a.(float64) > float64(b.(int)) {
                return a
            } else if a.(float64) < float64(b.(int)) {
                return b
            } else {
                return nil
            }
        case float64:
            if a.(float64) > b.(float64) {
                return a
            } else if a.(float64) < b.(float64) {
                return b
            } else {
                return nil
            }
        case string:
            if a.(float64) > float64(strconv.ParseFloat(strings.Replace(b.(string), ",", "", -1), 64)) {
                return a
            } else if a.(float64) < float64(strconv.ParseFloat(strings.Replace(b.(string), ",", "", -1), 64)) {
                return b
            } else {
                return nil
            }
        }
    case string:
        switch b.(type) {
        case int:
            if strings.Replace(a.(string), ",", "", -1) > strconv.Itoa(b.(int)) {
                return a
            } else if strings.Replace(a.(string), ",", "", -1) < strconv.Itoa(b.(int)) {
                return b
            } else {
                return nil
            }
        case float64:
            if strings.Replace