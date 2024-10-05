    public String wordsInSentence(String sentence) {
        String[] words = sentence.split(" ");
        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (isPrime(word.length())) {
                result.add(word);
            }
        }
        return String.join(" ", result);
    }

    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

The solution above defines a method `wordsInSentence` that takes a sentence as input and returns a new string containing only the words from the original sentence whose lengths are prime numbers. The method splits the input sentence into words using the `split` method, and then iterates over the words using a for-each loop. For each word, it checks if the length of the word is prime using the `isPrime` method. If the length is prime, the word is added to a list. Finally, the method returns a string containing the words from the list, separated by spaces, using the `join` method.

The `isPrime` method checks if a given integer `n` is prime. It returns `true` if `n` is prime and `false` otherwise. The method first checks if `n` is less than or equal to 1, in which case it is not prime. Then it iterates over the numbers from 2 to the square root of `n`, and checks if `n` is divisible by any of these numbers. If `n` is divisible, it is not prime. If `n` is not divisible by any of the numbers in the loop, it is prime. The method returns `true` if `n` is prime and `false` otherwise.