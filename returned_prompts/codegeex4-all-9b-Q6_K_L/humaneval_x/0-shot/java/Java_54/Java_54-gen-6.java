```java
        Set<Character> set = new HashSet<Character>();
        for (char c : s0.toCharArray()) {
            set.add(c);
        }
        for (char c : s1.toCharArray()) {
            if (!set.contains(c)) {
                return false;
            }
        }
        return true;
    }
}
```