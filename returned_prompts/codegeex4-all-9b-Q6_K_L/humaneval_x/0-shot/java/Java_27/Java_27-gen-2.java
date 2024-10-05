```java
public String flipCase(String string) {
    return string.chars()
                 .map(Character::isLowerCase ? Character::toUpperCase : Character::toLowerCase)
                 .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
                 .toString();
}
```