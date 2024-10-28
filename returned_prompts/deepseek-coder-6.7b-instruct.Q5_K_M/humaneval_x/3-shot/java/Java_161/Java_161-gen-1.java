        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    chars[i] = Character.toLowerCase(c);
                } else {
                    chars[i] = Character.toUpperCase(c);
                }
            }
        }
        return new String(chars);
    }
}
```

## Answers

```
