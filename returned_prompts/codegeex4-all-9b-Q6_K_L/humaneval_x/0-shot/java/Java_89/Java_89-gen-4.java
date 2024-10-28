```java
public String encrypt(String s) {
        Map<Character, Character> map = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            map.put((char) ('a' + i), (char) ('a' + (i + 4) % 26));
        }
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                sb.append(map.get(c));
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
```
This solution uses a `HashMap` to store the mappings from each letter to its encrypted counterpart. It then iterates over each character in the input string and appends the corresponding encrypted character to a `StringBuilder`. If the character is not in the `HashMap`, it is appended as is. Finally, the `StringBuilder` is converted to a string and returned.