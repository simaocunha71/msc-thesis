        String[] words = s.split(" ");
        List<String> sorted_words = new ArrayList<>();

        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            sorted_words.add(String.valueOf(chars));
        }
        return String.join(" ", sorted_words);
    }
}

