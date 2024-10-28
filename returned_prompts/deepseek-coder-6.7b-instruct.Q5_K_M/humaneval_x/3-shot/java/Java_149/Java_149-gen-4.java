        List<String> evenLengthWords = new ArrayList<>();
        for (String word : lst) {
            if (word.length() % 2 == 0) {
                evenLengthWords.add(word);
            }
        }
        Collections.sort(evenLengthWords);
        return evenLengthWords;
    }
}

