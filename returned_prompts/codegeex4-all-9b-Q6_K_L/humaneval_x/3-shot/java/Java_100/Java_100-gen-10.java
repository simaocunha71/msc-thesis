        List<Integer> result = new ArrayList<>();
        int stones = n;
        result.add(stones);

        for (int i = 0; i < n - 1; i++) {
            if (stones % 2 == 0) {
                stones += 2;
            } else {
                stones += 2;
            }
            result.add(stones);
        }
        return result;
    }
}

