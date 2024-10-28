        Map<Integer, Integer> count_map = new HashMap<>();
        int result = -1;

        for (int i : lst) {
            count_map.put(i, count_map.getOrDefault(i, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : count_map.entrySet()) {
            int key = entry.getKey();
            int value = entry.getValue();

            if (key <= value && key > result) {
                result = key;
            }
        }
        return result;
    }
}

