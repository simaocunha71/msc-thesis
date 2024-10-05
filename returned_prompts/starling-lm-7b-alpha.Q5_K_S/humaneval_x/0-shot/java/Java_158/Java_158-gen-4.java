        String maxString = words.get(0);
        for (String s : words) {
            int[] uniqueChars = new int[26];
            for (char c : s.toCharArray()) {
                uniqueChars[c - 'a']++;
            }

            int numUnique = 0;
            for (int u : uniqueChars) {
                if (u == 1) {
                    numUnique++;
                }
            }

            if (numUnique > maxString.length() || (numUnique == maxString.length() && s.compareTo(maxString) < 0)) {
                maxString = s;
            }
        }
        return maxString;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.findMax(Arrays.asList("name", "of", "string"))); // "string"
        System.out.println(solution.findMax(Arrays.asList("name", "enam", "game"))); // "enam"
        System.out.println(solution.findMax(Arrays.asList("aaaaaaa", "bb", "cc"))); // "aaaaaaa"
    }
}
















































































































































































































