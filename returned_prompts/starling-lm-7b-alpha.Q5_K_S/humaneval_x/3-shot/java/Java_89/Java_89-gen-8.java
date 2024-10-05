        StringBuilder encrypted_string = new StringBuilder();
        for (char c : s.toCharArray()) {
            char original_char = c;
            if (c >= 'a' && c <= 'z') {
                c = (char) (c + 2 * 2);
                if (c > 'z') c = (char) (c - 'z' - 'a' + 'A');
                encrypted_string.append(c);
            } else if (c >= 'A' && c <= 'Z') {
                c = (char) (c + 2 * 2);
                if (c > 'Z') c = (char) (c - 'Z' - 'A' + 'a');
                encrypted_string.append(c);
            } else {
                encrypted_string.append(original_char);
            }
        }
        return encrypted_string.toString();
    }
}


public class Main {
    public static void main(String[] args) {
        // write your code here
        Solution solution = new Solution();
    }
}

```