        Set<Integer> odds = new TreeSet<>();
        while(n != 1) {
            if(n % 2 != 0) {
                odds.add(n);
            }
            n = n % 2 == 0 ? n / 2 : 3 * n + 1;
        }
        odds.add(1); // add 1 as the last number in the sequence
        return new ArrayList<>(odds);
     }
}

