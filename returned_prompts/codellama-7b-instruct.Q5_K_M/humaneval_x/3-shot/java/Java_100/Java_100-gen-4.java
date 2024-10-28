        List<Integer> result = new ArrayList<>();
        int stones_in_level = n;

        while (stones_in_level > 0) {
            result.add(stones_in_level);
            stones_in_level = (stones_in_level % 2 == 0) ? stones_in_level + 1 : stones_in_level + 3;
        }
        return result;
    }
}

