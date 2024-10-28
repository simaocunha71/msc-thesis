        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));

        for (int i = word.length() - 2; i > 0; i--) {
            if (vowels.contains(word.charAt(i)) && !vowels.contains(word.charAt(i - 1)) && !vowels.contains(word.charAt(i + 1))) {
                return String.valueOf(word.charAt(i));
            }
        }
        return "";
    }
}

