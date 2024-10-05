        List<Integer> pile = new ArrayList<>();
        int stones = n;
        for (int i = 0; i < n; i++) {
            pile.add(stones);
            if (stones % 2 == 0) {
                stones += n + 2 * i;
            } else {
                stones += n + 2 * i;
            }
        }
        return pile;
    }
}

