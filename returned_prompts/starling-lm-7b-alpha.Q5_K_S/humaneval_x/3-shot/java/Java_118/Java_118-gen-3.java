        List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
        int left = -1;
        int right = word.length();
        while (left + 1 < right) {
            int middle = (left + right) / 2;
            char c = word.charAt(middle);
            if (vowels.contains(c)) {
                right = middle;
            } else {
                left = middle;
            }
        }
        left += 1;
        while (left < word.length()) {
            char c = word.charAt(left);
            if (vowels.contains(c)) {
                return String.valueOf(c);
            }
            left += 1;
        }
        return "";
    }
}

