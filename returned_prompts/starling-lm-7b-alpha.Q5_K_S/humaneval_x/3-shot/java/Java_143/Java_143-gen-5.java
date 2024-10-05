        List<String> words = new ArrayList<>(Arrays.asList(sentence.split(" ")));
        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (isPrime(word.length())) {
                result.add(word);
            }
        }
        return String.join(" ", result);
    }

    private boolean isPrime(int number) {
        if (number < 2) return false;
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}

