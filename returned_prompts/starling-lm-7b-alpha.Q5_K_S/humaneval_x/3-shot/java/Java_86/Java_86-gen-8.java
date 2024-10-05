        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();
        for (String word : words) {
            result.append(sortWord(word)).append(" ");
        }
        return result.toString().trim();
    }

    public String sortWord(String word) {
        StringBuilder result = new StringBuilder();
        for (char c : word.toCharArray()) {
            result.append((char) (c - 1));
        }
        return result.toString();
    }
}

public class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.antiShuffle("Hello World!!!!"));
    }
}

```