```java
public boolean correctBracketing(String brackets) {
    int balance = 0;
    for (int i = 0; i < brackets.length(); i++) {
        if (brackets.charAt(i) == '<') {
            balance++;
        } else if (brackets.charAt(i) == '>') {
            balance--;
        }
        if (balance < 0) {
            return false;
        }
    }
    return balance == 0;
}
```