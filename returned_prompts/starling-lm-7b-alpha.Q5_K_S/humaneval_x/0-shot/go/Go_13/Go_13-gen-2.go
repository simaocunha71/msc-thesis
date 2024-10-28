
To calculate the greatest common divisor of two integers a and b, you can use the Euclidean algorithm. Here's how you can implement it in Swift:

```swift
func GreatestCommonDivisor(a: Int, b: Int) -> Int {
    if a == 0 {
        return b
    }
    return GreatestCommonDivisor(a: b % a, b: a)
}
```

In this function, we use a recursive approach. The base case is when `a` becomes 0. At this point, the greatest common divisor of `a` and `b` is equal to `b`. Otherwise, we update `a` to `b % a` and `b` to `a`, and recursively call the `GreatestCommonDivisor` function with the new values. This process continues until `a` becomes 0.

For example, if you call `GreatestCommonDivisor(3, 5)`, the function will return 1 because 1 is the greatest common divisor of 3 and 5. Similarly, if you call `GreatestCommonDivisor(25, 15)`, the function will return 5 because 5 is the greatest common divisor of 25 and 15.

```swift
print(GreatestCommonDivisor(3, 5)) // 1
print(GreatestCommonDivisor(25, 15)) // 5
```

This function should work correctly for any positive integer inputs.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```