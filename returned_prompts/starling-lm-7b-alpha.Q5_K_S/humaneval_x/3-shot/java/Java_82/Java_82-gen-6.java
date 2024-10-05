        Set<Integer> divisors = new HashSet<>();

        for (int i = 2; i * i <= string.length(); i++) {
            if (string.length() % i == 0) {
                divisors.add(i);
            }
        }
        return divisors.size() == 0;
    }
}

