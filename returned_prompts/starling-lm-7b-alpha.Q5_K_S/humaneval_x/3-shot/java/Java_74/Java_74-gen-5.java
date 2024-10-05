        if (lst1.size() < lst2.size()) {
            return lst1;
        } else if (lst2.size() < lst1.size()) {
            return lst2;
        } else {
            int total_chars_1 = 0;
            int total_chars_2 = 0;

            for (String s : lst1) {
                total_chars_1 += s.length();
            }

            for (String s : lst2) {
                total_chars_2 += s.length();
            }

            if (total_chars_1 < total_chars_2) {
                return lst1;
            } else {
                return lst2;
            }
        }
    }
}

public class A {
    public static void main(String[] args) {
        Solution solution = new Solution();
    }
}
```