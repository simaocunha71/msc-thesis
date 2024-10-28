        List<Integer> pile = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (n % 2 == 0) {
                pile.add(n + 2 * i);
            } else {
                pile.add(n + 2 * i);
            }
        }
        return pile;
    }
}

