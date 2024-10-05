Here is the solution:

```java
public String removeVowels(String text) {
    return text.replaceAll("[aeiouAEIOU]", "");
}
```

This function uses regular expressions to replace all vowels in the input string with an empty string, effectively removing them.