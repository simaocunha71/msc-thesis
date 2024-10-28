        List<String> words = new ArrayList<>(Arrays.asList(sentence.split(" ")));
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            if (isPrime(word.length())) {
                result.append(word).append(" ");
            }
        }
        return result.toString().trim();
    }

    public boolean isPrime(int n) {
        if (n < 2) return false;

        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

