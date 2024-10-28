```java
public String encode(String message) {
    return message.chars()
            .mapToObj(c -> {
                if (Character.isAlphabetic(c)) {
                    if (Character.isLowerCase(c)) {
                        if ("aeiou".indexOf(Character.toLowerCase(c)) != -1) {
                            return (char) (c + 2);
                        } else {
                            return Character.toUpperCase(c);
                        }
                    } else {
                        if ("AEIOU".indexOf(Character.toUpperCase(c)) != -1) {
                            return (char) (c - 2);
                        } else {
                            return Character.toLowerCase(c);
                        }
                    }
                }
                return c;
            })
            .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
            .toString();
}
```