        int result = 0;
        Set<Character> primes = new HashSet<>();
        primes.add('2');
        primes.add('3');
        primes.add('5');
        primes.add('7');
        primes.add('B');
        primes.add('C');
        primes.add('D');
        primes.add('E');
        primes.add('F');

        for (char c : num.toUpperCase().toCharArray()) {
            if (primes.contains(c)) {
                result += 1;
            }
        }
        return result;
    }
}

