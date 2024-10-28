Here is a Java function that satisfies the given conditions:

```java
public boolean anyInt(Object x, Object y, Object z) {
    if (!(x instanceof Integer && y instanceof Integer && z instanceof Integer)) {
        return false;
    }
    int a = (int) x;
    int b = (int) y;
    int c = (int) z;
    return (a == b + c) || (a == c + b) || (b == a + c) || (b == c + a) || (c == a + b) || (c == b + a);
}
```

This function first checks if all the input objects are instances of Integer. If not, it returns false. Then it casts the objects to int and checks if one of the numbers is equal to the sum of the other two. If it finds such a combination, it returns true. If it doesn't find such a combination, it returns false. 

This function handles both positive and negative integers, as well as the case where all three numbers are equal. It also handles the case where the input objects are not instances of Integer, in which case it returns false. 

For example, anyInt(5, 2, 7) returns true, because 5 is equal to 2 + 7. On the other hand, anyInt(3, 2, 2) returns false, because none of the numbers are equal to the sum of the other two. 

This function also correctly handles non-integer inputs, such as anyInt(3.6, -2.2, 2), which returns false, because the inputs are not integers. 

Note that this function uses the "instanceof" operator to check if an object is an instance of a certain class, and the cast operator to convert an object to a certain type. The "instanceof" operator is used to check if an object is an instance of a certain class, and the cast operator is used to convert an object to a certain type. The cast operator is used to convert an object to a certain type. 

The "instanceof" operator is a binary operator that takes two operands. The first operand is the object that you want to check, and the second operand is the class that you want to check against. The "instanceof" operator returns true if the object is an instance of the class, and false otherwise. 

The cast operator is a unary operator that takes one operand. The operand