        Map<Integer, Integer> count_map = new HashMap<>();
        List<Integer> result = new ArrayList<>();

        for (Integer number : numbers) {
            if (count_map.containsKey(number)) {
                count_map.put(number, count_map.get(number) + 1);
            } else {
                count_map.put(number, 1);
            }
        }

        for (Integer number : numbers) {
            if (count_map.get(number) == 1) {
                result.add(number);
            }
        }
        return result;
    }
}

