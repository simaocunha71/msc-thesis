        List<String> words = Arrays.asList(sentence.split(" "));
        Set<Integer> primes = new HashSet<>();
        for (int i = 2; i < 100; i++) {
            if (isPrime(i)) {
                primes.add(i);
            }
        }
        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (primes.contains(word.length())) {
                result.add(word);
            }
        }
        return String.join(" ", result);
    }

    private boolean isPrime(int n) {
        if (n == 2) return true;
        if (n % 2 == 0 || n < 2) return false;
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}


class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));

        // Example 2
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));

        // Example 3
        System.out.println(solution.truncateNumber(3.5));

        // Example 4
        System.out.println(solution.wordsInSentence("This is a test"));
        System.out.println(solution.wordsInSentence("lets go for swimming"));
    }
}

```