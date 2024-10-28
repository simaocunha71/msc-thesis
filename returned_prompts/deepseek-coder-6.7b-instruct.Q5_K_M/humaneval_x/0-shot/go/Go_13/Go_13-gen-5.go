
// Find the absolute value of a
a = Abs(a)

B:

// Find the absolute value of b
b = Abs(b)

C:

// If a equals zero, return b
if a == 0 {
return b
}

D:

// If b equals zero, return a
if b == 0 {
return a
}

E:

// If a is greater than b, set a to a mod b
if a > b {
a = a % b
goto C
}

F:

// If b is greater than a, set b to b mod a
if b > a {
b = b % a
goto C
}

G:

// Return the greatest common divisor
return a
}

```

## 4. 对数组的处理

