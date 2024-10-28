You can solve this problem by converting the integer to a string and then checking each character. If the character is an odd digit, you multiply it to the product. Here is the Java solution:

```java
public int digits(int n) {
    int product = 1;
    boolean hasOdd = false;
    String str = Integer.toString(n);
    for (int i = 0; i < str.length(); i++) {
        char c = str.charAt(i);
        int digit = c - '0';
        if (digit % 2 != 0) {
            product *= digit;
            hasOdd = true;
        }
    }
    return hasOdd ? product : 0;
}
```

This solution first initializes the product to 1 and a boolean variable hasOdd to false. Then it converts the integer to a string and iterates over each character. If the character is an odd digit, it multiplies it to the product and sets hasOdd to true. Finally, it returns the product if hasOdd is true, otherwise it returns 0.