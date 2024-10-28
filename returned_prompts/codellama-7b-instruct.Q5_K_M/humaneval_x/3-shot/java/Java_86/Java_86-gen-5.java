        String[] words = s.split(" ");

        StringBuilder result = new StringBuilder();
        for (String word : words) {
            char[] letters = word.toCharArray();
            Arrays.sort(letters);
            result.append(String.valueOf(letters));
            result.append(" ");
        }
        return result.toString().trim();
    }
}

