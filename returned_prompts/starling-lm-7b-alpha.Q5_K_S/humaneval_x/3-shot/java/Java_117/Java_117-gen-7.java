        List<String> result = new ArrayList<>();
        boolean is_consonant;
        char c;
        int count;
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            is_consonant = (c != ' ' && c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u');
            count = 0;
            while (i < s.length() && (is_consonant || count == n)) {
                if (is_consonant) count += 1;
                i += 1;
                if (i < s.length()) c = s.charAt(i);
                is_consonant = (c != ' ' && c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u');
            }
            if (count == n) result.add(s.substring(i - count, i));
        }
        return result;
    }
}


public class ProblemSolving {
    public static void main(String[] args) {
        Solution solution = new Solution();
    }
}

```