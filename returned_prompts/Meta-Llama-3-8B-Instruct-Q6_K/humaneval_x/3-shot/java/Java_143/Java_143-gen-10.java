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
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

