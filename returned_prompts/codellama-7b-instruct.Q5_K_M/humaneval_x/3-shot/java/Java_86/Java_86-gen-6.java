        String[] words = s.split(" ");

        List<String> result = new ArrayList<>();

        for (String word : words) {
            char[] word_chars = word.toCharArray();
            Arrays.sort(word_chars);
            result.add(new String(word_chars));
        }

        return String.join(" ", result);
    }
}

