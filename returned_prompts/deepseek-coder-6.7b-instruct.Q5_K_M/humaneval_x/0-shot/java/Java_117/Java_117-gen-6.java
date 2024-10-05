    List<String> words = Arrays.asList(s.split(" "));
    List<String> selectedWords = new ArrayList<>();

    for (String word : words) {
        int consonants = 0;
        for (char c : word.toCharArray()) {
            if (!"aeiouAEIOU".contains(String.valueOf(c))) {
                consonants++;
            }
        }
        if (consonants == n) {
            selectedWords.add(word);
        }
    }

    return selectedWords;
}
}

*/

/*

