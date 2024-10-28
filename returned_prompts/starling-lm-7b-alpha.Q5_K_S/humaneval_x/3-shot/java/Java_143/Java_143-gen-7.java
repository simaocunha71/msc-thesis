        List<String> words = Arrays.asList(sentence.split(" "));
        List<String> primes = new ArrayList<>();
        for (int i = 0; i < words.size(); i++) {
            if (isPrime(words.get(i).length())) {
                primes.add(words.get(i));
            }
        }
        return String.join(" ", primes.toArray(new String[0]));
    }

    private boolean isPrime(int n) {
        if (n == 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

