        List<String> words = Arrays.asList(sentence.split(" "));
        List<String> prime_words = new ArrayList<>();
        int sentence_length = sentence.length();

        for (String word : words) {
            int word_length = word.length();
            if (is_prime(word_length)) {
                prime_words.add(word);
            }
        }

        return String.join(" ", prime_words);
    }

    private boolean is_prime(int x) {
        if (x == 2) return true;
        if (x % 2 == 0) return false;
        for (int i = 3; i * i <= x; i += 2) {
            if (x % i == 0) return false;
        }
        return true;
    }
}


```