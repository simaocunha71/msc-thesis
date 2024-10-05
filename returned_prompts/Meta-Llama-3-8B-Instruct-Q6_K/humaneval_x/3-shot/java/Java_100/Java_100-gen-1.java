        List<Integer> result = new ArrayList<>();
        int level = 1;
        int stones = n;

        while (stones > 0) {
            result.add(0, stones);
            stones = level * (level % 2 == 0 ? 2 : 2 - 1);
            level++;
        }
        return result;

    }
}

