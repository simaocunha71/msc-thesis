    public String antiShuffle(String s) {
        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();

        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            sb.append(new String(chars)).append(" ");
        }

        return sb.toString().trim();
    }
    // Time complexity: O(n*m log m)
    // where n is the number of words and m is the maximum length of a word.
    // Space complexity: O(n*m) for the output string and O(m) for the sorting.