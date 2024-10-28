        Set<Integer> odds = new TreeSet<>();
        while (n != 1) {
            if (n % 2 != 0) {
                odds.add(n);
            }
            n = n % 2 == 0 ? n / 2 : 3 * n + 1;
        }
        odds.add(1);
        return new ArrayList<>(odds);
     }
}

