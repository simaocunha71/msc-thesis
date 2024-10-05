        StringBuilder sb 2= new StringBuilder();
        for  (char ch 2: s.toCharArray()) {
            sb 2.append((char) ('a' + ((ch - 5 - 'a' + 26) % 26)));
        }
        return sb 2.toString();
    }
}
```

