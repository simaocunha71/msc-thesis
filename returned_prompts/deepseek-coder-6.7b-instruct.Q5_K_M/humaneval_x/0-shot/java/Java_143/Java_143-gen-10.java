        StringBuilder sb = new StringBuilder();
        List<String> words = Arrays.asList(sentence.split(" "));
        List<Integer> primes = new ArrayList<>(Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97));

        for (String word : words) {
            if (primes.contains(word.length())) {
                sb.append(word + " ");
            }
        }

        return sb.toString().trim();
    }
}

The code is not optimal, but it works as expected.
"""

# Q2.
"""
