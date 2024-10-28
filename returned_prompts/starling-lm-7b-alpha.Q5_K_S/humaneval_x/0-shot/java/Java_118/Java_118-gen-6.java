
        List<Character> list = Arrays.asList('a', 'e', 'i', 'o', 'u');
        char[] chars = word.toCharArray();
        int min = Integer.MAX_VALUE;
        char res = ' ';

        for (int i = 0; i < chars.length; i++) {
            if (list.contains(Character.toLowerCase(chars[i]))) {
                int left = i - 1;
                int right = i + 1;
                while (left >= 0 && Character.isAlphabetic(chars[left])) {
                    left--;
                }
                while (right < chars.length && Character.isAlphabetic(chars[right])) {
                    right++;
                }
                if (left + 1 + right == chars.length - i) {
                    break;
                }
                if (right - left < min) {
                    min = right - left;
                    res = chars[i];
                }
            }
        }
        return String.valueOf(res);
    }
}























































```



```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
