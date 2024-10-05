        List<String> words = Arrays.asList(sentence.split(" "));
        List<String> prime_words = new ArrayList<>();

        for (String word : words) {
            if (isPrime(word.length())) {
                prime_words.add(word);
            }
        }
        return String.join(" ", prime_words);
    }

    public boolean isPrime(int num) {
        if (num == 1) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

