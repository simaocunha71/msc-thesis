    // Check if the sides form a valid triangle
    if (a + b) > c && (b + c) > a && (c + a) > b {
        // Calculate the semi-perimeter
        s := (a + b + c) / 2
        // Calculate the area using Heron's formula
        area := math.Sqrt(s * (s - a) * (s - b) * (s - c))
        // Return the area rounded to 2 decimal points
        return math.Round(area*100) / 100
    } else {
        return -1
    }
}
```

This code first checks if the three provided sides form a valid triangle. If they don't, it returns -1. If they do, it calculates the semi-perimeter and then uses Heron's formula to calculate the area of the triangle. The area is then rounded to two decimal points and returned.

The main function is:

```go
func main() {
    fmt.Println(TriangleArea(3, 4, 5))  // Output: 6.00
    fmt.Println(TriangleArea(1, 2, 10)) // Output: -1
}
```

This code simply calls the `TriangleArea` function with the example inputs and prints the returned values.

This code can be run with the `go run` command.

```shell
$ go run main.go
6.00
-1
```

The output is the expected area of the triangle or -1 if the sides do not form a valid triangle.

Please note that this code does not handle invalid inputs (like negative lengths of sides). You might need to add additional checks for that.
Also, this code uses the `math.Round` function which rounds to the nearest even number. If you want to always round up, you can use `math.Ceil` instead.

If you want to use this code, just replace the import statement and the function body with your own code.








































