        List<String> evenLengthWords = new ArrayList<>();
        for (String word : lst) {
            if (word.length() % 2 == 0) {
                evenLengthWords.add(word);
            }
        }

        Collections.sort(evenLengthWords, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if (s1.length() != s2.length()) {
                    return s1.length() - s2.length();
                } else {
                    return s1.compareTo(s2);
                }
            }
        });

        return evenLengthWords;
    }
}

