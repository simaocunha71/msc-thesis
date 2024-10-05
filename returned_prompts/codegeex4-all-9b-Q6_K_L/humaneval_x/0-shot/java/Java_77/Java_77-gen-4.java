```java
public boolean iscube(int a) {
    int x = (int) Math.cbrt(a);
    return x * x * x == a;
}
```
This function first calculates the cube root of the input number a using the Math.cbrt() function and casts it to an integer. Then it checks if the cube of the integer is equal to the input number a. If it is, the function returns true, otherwise it returns false.