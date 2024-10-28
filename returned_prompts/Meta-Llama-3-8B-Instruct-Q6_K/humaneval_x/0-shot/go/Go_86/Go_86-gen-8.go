```go
package main

import (
    "fmt"
    "sort"
    "strings"
)

func AntiShuffle(s string) string {
    words := strings.Split(s, " ")
    var result []string
    for _, word := range