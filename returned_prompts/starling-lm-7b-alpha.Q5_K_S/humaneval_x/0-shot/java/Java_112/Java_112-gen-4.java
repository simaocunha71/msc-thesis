    StringBuilder sb = new StringBuilder();
    boolean isPalindrome = true;

    for(int i = 0; i < s.length(); i++) {
        char ch = s.charAt(i);
        if(!c.contains(String.valueOf(ch))) {
            sb.append(ch);
        } else {
            isPalindrome = false;
        }
    }

    String tmp = sb.reverse().toString();
    return Arrays.asList(sb.toString(), isPalindrome && tmp.equals(sb.toString()));
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

```

``