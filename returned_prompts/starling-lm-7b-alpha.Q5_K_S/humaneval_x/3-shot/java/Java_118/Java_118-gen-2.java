        List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
        List<Character> consonants = new ArrayList<>();

        for (char c : word.toCharArray()) {
            if (vowels.contains(c)) return "";
            consonants.add(c);
        }

        if (consonants.size() < 2) return "";

        int index_1 = consonants.indexOf(consonants.get(consonants.size() - 1));
        int index_2 = consonants.indexOf(consonants.get(consonants.size() - 2));

        if (index_1 > index_2) {
            index_1 = consonants.size() - index_1 - 1;
            index_2 = consonants.size() - index_2 - 1;
        }

        int index = 0;
        for (int i = 0; i < consonants.size(); i++) {
            if (consonants.get(i) == consonants.get(index_1) || consonants.get(i) == consonants.get(index_2)) {
                index = i;
            }
        }

        for (char c : consonants) {
            if (vowels.contains(c)) {
                return c + "";
            }
        }

        return "";
    }
}

