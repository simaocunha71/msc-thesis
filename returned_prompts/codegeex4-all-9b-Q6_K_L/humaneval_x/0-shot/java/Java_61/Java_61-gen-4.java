```java
public boolean correctBracketing(String brackets) {
    int balance = 0;
    for (char c : brackets.toCharArray()) {
        if (c == '(') {
            balance++;
        } else if (c == ')') {
            balance--;
        }
        if (balance < 0) {
            return false;
        }
    }
    return balance == 0;
}
```