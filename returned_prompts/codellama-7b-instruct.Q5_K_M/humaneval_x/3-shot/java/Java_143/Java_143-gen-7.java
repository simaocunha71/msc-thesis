        List<String> result = new ArrayList<>();
        String[] words = sentence.split(" ");
        for (String word : words) {
            if (isPrime(word.length())) result.add(word);
        }
        return String.join(" ", result);
    }

    public boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

