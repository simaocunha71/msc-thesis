        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            StringBuilder wordBuilder = new StringBuilder();
            for (char c : word.toCharArray()) {
                wordBuilder.append((char) (c - 128));
            }
            result.append(wordBuilder.toString()).append(" ");
        }

        return result.toString().trim();
    }
}

