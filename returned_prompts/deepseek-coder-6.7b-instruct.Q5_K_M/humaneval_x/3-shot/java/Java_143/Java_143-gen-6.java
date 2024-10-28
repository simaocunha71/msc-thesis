        List<String> words = Arrays.asList(sentence.split(" "));
        StringBuilder res = new StringBuilder();

        for (String word : words) {
            if (isPrime(word.length())) {
                res.append(word).append(" ");
            }
        }

        return res.toString().trim();
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

