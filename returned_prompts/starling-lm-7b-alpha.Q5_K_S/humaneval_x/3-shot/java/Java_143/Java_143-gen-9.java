        List<String> words = Arrays.asList(sentence.split(" "));
        List<String> prime_length_words = new ArrayList<>();
        for (String word : words) {
            if (isPrime(word.length())) {
                prime_length_words.add(word);
            }
        }
        return String.join(" ", prime_length_words);
    }

    private boolean isPrime(int number) {
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}

