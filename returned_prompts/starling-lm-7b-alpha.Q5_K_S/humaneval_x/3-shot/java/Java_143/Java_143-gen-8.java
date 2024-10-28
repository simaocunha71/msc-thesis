        List<String> words = Arrays.asList(sentence.split(" "));
        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (isPrime(word.length())) {
                result.add(word);
            }
        }
        return String.join(" ", result);
    }

    public boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

