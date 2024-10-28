        List<String> prime_word_list = new ArrayList<>();
        String[] words = sentence.split(" ");
        for (String word : words) {
            int length = word.length();
            if (isPrime(length)) {
                prime_word_list.add(word);
            }
        }
        return String.join(" ", prime_word_list);
    }

    public boolean isPrime(int n) {
        if (n == 1) return false;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

