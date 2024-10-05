        List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u');
        int prev_index = -1;
        int next_index = -1;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (vowels.contains(c)) {
                prev_index = next_index;
                next_index = i;
            }
        }
        return prev_index == -1 || next_index == -1 ? "" : String.valueOf(word.charAt(next_index));
    }
}

