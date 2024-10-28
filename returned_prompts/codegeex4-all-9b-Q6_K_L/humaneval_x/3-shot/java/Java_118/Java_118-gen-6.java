        Set<Character> vowels = new HashSet<>(Arrays.asList('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'));
        for (int i = word.length() - 1; i >= 0; i--) {
            char c = word.charAt(i);
            if (vowels.contains(c)) {
                return Character.toString(c);
            }
        }
        return "";
    }
}

