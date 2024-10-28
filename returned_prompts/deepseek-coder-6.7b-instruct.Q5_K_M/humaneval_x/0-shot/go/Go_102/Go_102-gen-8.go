
  if x > y {
    return -1
  }
  if x%2 == 0 {
    return x
  }
  x++
  goto A
}
```

The code will increment x until it is even. If no even number in the range [x, y] exists, the function will return -1.

As we know, in Go there's no goto statement, so we can't use it to jump to the label. But we can achieve the same effect using recursion.

```go
func ChooseNum(x, y int) int {
  if x > y {
    return -1
  }
  if x % 2 == 0 {
    return x
  }
  return ChooseNum(x+1, y)
}
```

This version of the function works by recursively calling itself with x+1 until it finds an even number or until x > y, in which case it returns -1.

Note that the recursion depth is limited, so for large ranges this could cause a stack overflow.

Also, in this problem it's not really important to use goto, as this problem is more about understanding the concept of recursion and how it can be used to solve a problem rather than about the Go language itself.































































































































































































































