
	str := strconv.Itoa(x)
	res := ""
	if shift >= len(str) {
		for _, v := range str {
			res = string(v) + res
		}
		return res
	}
	res = str[len(str)-shift:] + str[:len(str)-shift]
	return res
}

```

---

## 10. 3D Perimeter and Volume of a Box

Given the length, width and height of a box. Your task is to write a function to calculate its 3D perimeter and volume.

The formula for the 3D perimeter of a box is:

Perimeter = 2lw + 2lh + 2wh

The formula for the volume of a box is:

Volume = lwh

Here, l, w and h represent the length, width and height of the box respectively.

Here is a Python code to solve the problem:

```python
def box_dimensions(l, w, h):
    perimeter = 2*l*w + 2*l*h + 2*w*h
    volume = l*w*h
    return perimeter, volume
```

And here is a Golang code:

```go
package main

import "fmt"

func BoxDimensions(l int, w int, h int) (int, int) {
    perimeter := 2*l*w + 2*l*h + 2*w*h
    volume := l*w*h
    return perimeter, volume
}

func main() {
    l, w, h := 10, 5, 7
    perimeter, volume := BoxDimensions(l, w, h)
    fmt.Printf("Perimeter: %d\nVolume: %d\n", perimeter, volume)
}
```

---

## 11. Sum of all numbers in an array

Write a function that finds the sum of all numbers in an array.

Here is a Python code to solve the problem:

```python
def sum_array(arr):
    return sum(arr)
```

And here is a Gol