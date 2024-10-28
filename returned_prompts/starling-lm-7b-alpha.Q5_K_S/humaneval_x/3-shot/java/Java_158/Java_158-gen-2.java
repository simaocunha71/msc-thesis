        List<Character> unique_chars = new ArrayList<>();
        String max_word = "";
        int max_chars = 0;

        for (String word : words) {
            unique_chars.clear();
            for (char c : word.toCharArray()) {
                if (!unique_chars.contains(c)) {
                    unique_chars.add(c);
                }
            }
            if (unique_chars.size() > max_chars) {
                max_chars = unique_chars.size();
                max_word = word;
            }
        }
        return max_word;
    }
}


class Program {
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.findMax(Arrays.asList("name", "of", "string")));
        System.out.println(s.findMax(Arrays.asList("name", "enam", "game")));
        System.out.println(s.findMax(Arrays.asList("aaaaaaa", "bb", "cc")));
    }
}
```