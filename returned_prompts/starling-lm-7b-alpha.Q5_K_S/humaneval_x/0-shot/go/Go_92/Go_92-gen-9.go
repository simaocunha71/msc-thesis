
func AnyInt(x, y, z interface{}) bool {
    if reflect.TypeOf(x).Kind() == reflect.Int && reflect.TypeOf(y).Kind() == reflect.Int && reflect.TypeOf(z).Kind() == reflect.Int {
        if x.(int) == y.(int) + z.(int) || y.(int) == x.(int) + z.(int) || z.(int) == x.(int) + y.(int) {
            return true
        }
    }
    return false
}
































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

// Create a function that takes 3 numbers.
// Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
// Returns false in any other cases.
// 
// Examples
// AnyInt(5, 2, 7) ➞ true
// 
// AnyInt(3, 2, 2) ➞ false
// 
// AnyInt(3, -2, 1) ➞ true
// 
// AnyInt(3.6, -2.2, 2) ➞ false
func AnyInt(x, y, z interface{}) bool {
    if reflect.TypeOf(x).Kind() == reflect.Int && reflect.TypeOf(y).Kind() == reflect.Int && reflect.TypeOf(z).Kind() == reflect.Int {
        if x.(int) == y.(int) + z.(int) || y.(int) == x.(int) + z.(int) || z.(int) == x.(int) + y.(int) {
            return true
        }
    }
    return false
}
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
