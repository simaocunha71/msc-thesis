```
return math.Ceil(math.Cbrt(float64(a))) == math.Ceil(math.Cbrt(float64(a)))
```

Explanation:
The math.Cbrt function calculates the cube root of a number. The math.Ceil function rounds up the result to the nearest integer. So, if the input number `a` is a perfect cube, then the cube root of `a` will be an integer, and the math.Ceil function will return the same integer value as the math.Cbrt function. Otherwise, the math.Ceil function will return a different integer value. Therefore, we can check if the result of math.Ceil(math.Cbrt(float64(a))) is equal to the result of math.Ceil(math.Cbrt(float64(a))), if it is, then `a` is a perfect cube. If not, then `a` is not a perfect cube. This way, we can determine if `a` is a cube of some integer number or not. This approach is very efficient and works well for large inputs.