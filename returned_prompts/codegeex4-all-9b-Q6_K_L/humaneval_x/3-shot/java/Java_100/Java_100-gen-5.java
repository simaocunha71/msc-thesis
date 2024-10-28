        List<Integer> result = new ArrayList<>();
        int level = 1;
        int stones = n;

        while (stones > 0) {
            result.add(stones);
            stones += level;
            level += 2;
        }
        return result;

    }
}

