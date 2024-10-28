        List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
        for (int i = 1; i < word.length() - 1; i++) {
            if (vowels.contains(word.charAt(i))) {
                return word.charAt(i) + "";
            }
        }
        return "";
    }
}

