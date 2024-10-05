        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            char[] characters = word.toCharArray();
            Arrays.sort(characters);
            result.append(String.valueOf(characters)).append(" ");
        }
        return result.toString().trim();
    }
}

