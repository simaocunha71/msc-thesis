        String[] words = sentence.split(" ");
        String result = "";

        for (String word : words) {
            if (isPrime(word.length())) {
                result += word + " ";
            }
        }
        return result.trim();
    }

    boolean isPrime(int n) {
        if (n == 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

