        List<String> words = Arrays.asList(sentence.split(" "));
        List<String> prime_words = new ArrayList<>();

        for (String word : words) {
            if (isPrime(word.length())) {
                prime_words.add(word);
            }
        }
        return String.join(" ", prime_words);
    }

    private boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;

        for (int i = 5; i * i <= n; i = i + 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}

