```java
public boolean correctBracketing(String brackets) {
    Stack<Character> s = new Stack<>();
    for (char c : brackets.toCharArray()) {
        if (c == '(') {
            s.push(c);
        } else {
            if (s.isEmpty()) {
                return false;
            }
            s.pop();
        }
    }
    return s.isEmpty();
}
```