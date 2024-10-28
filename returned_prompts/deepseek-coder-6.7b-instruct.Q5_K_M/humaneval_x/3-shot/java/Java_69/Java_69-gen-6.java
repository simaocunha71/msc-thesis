        int result = -1;
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : lst) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            if (entry.getKey() < entry.getValue() && entry.getKey() > result) {
                result = entry.getKey();
            }
        }
        return result;
    }
}

