        List<String> prime_words = new ArrayList<>();
        for (String word : sentence.split(" ")) {
            if (isPrime(word.length())) {
                prime_words.add(word);
            }
        }
        return String.join(" ", prime_words);
    }

    private boolean isPrime(int n) {
        if (n == 1) return false;
        if (n == 2) return true;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

