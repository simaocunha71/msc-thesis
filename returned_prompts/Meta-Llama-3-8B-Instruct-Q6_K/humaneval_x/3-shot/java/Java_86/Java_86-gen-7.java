        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            StringBuilder sortedWord = new StringBuilder();
            for (char c : word.toCharArray()) {
                sortedWord.append((char) (c));
            }
            result.append(sortedWord).append(" ");
        }

        return result.toString().trim();
    }
}