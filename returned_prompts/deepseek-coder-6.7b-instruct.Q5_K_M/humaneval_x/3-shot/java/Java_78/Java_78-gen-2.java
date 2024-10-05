        Set<Character> primes = new HashSet<>(Arrays.asList('2', '3', '5', '7', 'B', 'D'));
        int count = 0;

        for (char c : num.toCharArray()) {
            if (primes.contains(c)) {
                count++;
            }
        }

        return count;
    }
}

