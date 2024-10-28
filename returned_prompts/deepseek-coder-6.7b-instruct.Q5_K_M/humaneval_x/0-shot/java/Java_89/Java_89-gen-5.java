        String result = "";

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (Character.isUpperCase(c)) {
                result += (char) ('A' + (c - 'A' + 2) % 26 * 2);
            } else {
                result += (char) ('a' + (c - 'a' + 2) % 26 * 2);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.encrypt("hi")); // "lm"
        System.out.println(solution.encrypt("asdfghjkl")); // "ewhjklnop"
        System.out.println(solution.encrypt("gf")); // "kj"
        System.out.println(solution.encrypt("et")); // "ix"
    }
}

```

### Java Programming: Caesar Cipher

```java
