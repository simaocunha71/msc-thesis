        int start = 0, end = string.length() - 1;
        while (start < end) {
            if (string.charAt(start) != string.charAt(end)) {
                StringBuilder sb = new StringBuilder(string.substring(start));
                StringBuilder sb2 = new StringBuilder(string.substring(0, start));
                sb2.reverse();
                return sb.append(sb2.toString()).toString();
            }
            start++;
            end--;
        }
        return string;
    }
}


























```
```

```

```