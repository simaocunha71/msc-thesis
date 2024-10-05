Here is a simple Java solution that uses the modulus operator to get the unit digits of the two numbers and then multiplies them:

```java
public int multiply(int a, int b) {
    return (a % 10) * (b % 10);
}
```
This solution works by taking the remainder when a is divided by 10 (which is the unit digit of a) and the remainder when b is divided by 10 (which is the unit digit of b), then multiplying these two numbers together.