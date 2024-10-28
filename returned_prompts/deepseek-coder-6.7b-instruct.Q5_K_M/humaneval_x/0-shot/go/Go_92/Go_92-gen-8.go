
    // Check if all inputs are integers.
    if xVal, ok := x.(int); !ok || yVal, ok := y.(int); !ok || zVal, ok := z.(int); !ok {
        return false
    }

B:

    // Check if one of the numbers is equal to the sum of the other two.
    if xVal+yVal == zVal || yVal+zVal == xVal || zVal+xVal == yVal {
        return true
    }

    return false
}

```

### C. [100 pts] Given a string, return the character that is most commonly used in the string.

```go
