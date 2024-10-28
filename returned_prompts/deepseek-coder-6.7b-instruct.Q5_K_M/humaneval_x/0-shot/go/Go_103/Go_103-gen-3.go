    if n > m {
        return -1
    }

B:
    avg := math.Round(float64(n+m) / 2)

C:
    return fmt.Sprintf("%b", int(avg))
}

func main() {
    fmt.Println(RoundedAvg(1, 5))
    fmt.Println(RoundedAvg(7, 5))
    fmt.Println(RoundedAvg(10, 20))
    fmt.Println(RoundedAvg(20, 33))
}

```

## Test cases

```go
func TestRoundedAvg(t *testing.T) {
    type test struct {
        input1, input2 int
        expected       interface{}
    }

    tests := []test{
        {1, 5, "0b11"},
        {7, 5, -1},
        {10, 20, "0b1111"},
        {20, 33, "0b11010"},
    }

    for _, test := range tests {
        got := RoundedAvg(test.input1, test.input2)
        if got != test.expected {
            t.Errorf("For inputs %d and %d, expected %v, but got %v", test.input1, test.input2, test.expected, got)
        }
    }
}
```

## Conclusion

The above code is a simple Go program that calculates the rounded average of two given integers and converts it to binary. It includes a test function to verify the output.

```go
func main() {
    fmt.Println(RoundedAvg(1, 5))
    fmt.Println(RoundedAvg(7, 5))
    fmt.Println(RoundedAvg(10, 20))
    fmt.Println(RoundedAvg(20, 33))
}
```

This main function calls the RoundedAvg function with various inputs to demonstrate its functionality.

```go
func TestRounded