        StringBuilder result = new StringBuilder();
        boolean space_seen = false;
        boolean hyphen_seen = false;
        for (char c : text.toCharArray()) {
            if (c == ' ') {
                if (space_seen) {
                    if (!hyphen_seen) {
                        hyphen_seen = true;
                        result.append('-');
                    }
                } else {
                    space_seen = true;
                    result.append('_');
                }
            } else {
                hyphen_seen = false;
                result.append(c);
                space_seen = false;
            }
        }
        return result.toString();
    }
}

public class CodeChallenge {

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.fixSpaces("Example   3"));
    }
}
```