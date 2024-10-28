```
return Math.cbrt(a) % 1 === 0;
```


The function `iscube` takes an integer `a` as input and returns a boolean value indicating whether `a` is a cube of some integer number or not.

The function uses the `Math.cbrt` method, which returns the cube root of a number. The `% 1 === 0` part checks whether the result of the cube root operation is an integer (i.e., whether the remainder when divided by 1 is 0). If the result is an integer, then `a` is a cube of some integer number, and the function returns `true`. Otherwise, it returns `false`.

The examples provided in the problem statement demonstrate that the function works correctly for different inputs. For instance, `iscube(1)` returns `true` because 1 is a cube of 1, and `iscube(64)` returns `true` because 64 is a cube of 4. On the other hand, `iscube(2)` returns `false` because 2 is not a cube of any integer number, and `iscube(180)` returns `false` because 180 is not a cube of any integer number either.