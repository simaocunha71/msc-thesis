        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (Integer num : lst) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        int max = -1;
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            if (entry.getKey() > 0 && entry.getValue() >= entry.getKey()) {
                max = Math.max(max, entry.getKey());
            }
        }
        return max;
    }
}

