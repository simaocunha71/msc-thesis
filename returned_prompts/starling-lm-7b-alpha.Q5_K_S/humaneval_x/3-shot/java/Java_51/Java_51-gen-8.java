        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        StringBuilder result = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (!vowels.contains(c)) {
                result.append(c);
            }
        }
        return result.toString();
    }
}

