        int max = 0;
        int maxCount = 0;
        Map<Integer, Integer> countMap = new HashMap<>();

        for (int num : lst) {
            if (countMap.containsKey(num)) {
                countMap.put(num, countMap.get(num) + 1);
            } else {
                countMap.put(num, 1);
            }
        }

        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            if (entry.getKey() > max && entry.getValue() >= entry.getKey()) {
                max = entry.getKey();
                maxCount = entry.getValue();
            }
        }

        return maxCount > 0 ? max : -1;
    }
}