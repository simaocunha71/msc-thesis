        String[] words = sentence.split(" ");
        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (isPrime(word.length())) {
                result.add(word);
            }
        }
        return String.join(" ", result);
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

