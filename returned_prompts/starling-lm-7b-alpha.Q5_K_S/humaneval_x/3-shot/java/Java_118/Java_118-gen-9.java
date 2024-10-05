        String vowels = "aeiou";
        List<Character> consonants = new ArrayList<>();
        List<Character> vowel_positions = new ArrayList<>();

        for (char c : word.toCharArray()) {
            if (vowels.indexOf(c) != -1) {
                vowel_positions.add(c);
            } else {
                consonants.add(c);
            }
        }

        if (consonants.size() < 2) return "";

        int left = consonants.indexOf(consonants.get(consonants.size() - 1));
        int right = consonants.indexOf(consonants.get(consonants.size() - 2));

        if (left == 0 && right == 0) return "";
        if (left == 0 && right == 1) {
            for (char c : vowel_positions) {
                if (c != word.charAt(1)) return String.valueOf(c);
            }
            return "";
        }
        if (left == 1 && right == 0) {
            for (char c : vowel_positions) {
                if (c != word.charAt(word.length() - 2)) return String.valueOf(c);
            }
            return "";
        }
        if (left > right) {
            for (char c : vowel_positions) {
                if (c != word.charAt(word.length() - 3)) return String.valueOf(c);
            }
            return "";
        } else {
            for (char c : vowel_positions) {
                if (c != word.charAt(1)) return String.valueOf(c);
            }
            return "";
        }

    }
}


public class A {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.getClosestVowel("ab"));
    }
}
```