        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            sb.append((char) ('a' + ((ch - 5) % 26)));
        }
        return sb.toString();
    }
}

public class A {
    public static void main(String[] args) {
        Solution solution = new Solution();
    }
}

```