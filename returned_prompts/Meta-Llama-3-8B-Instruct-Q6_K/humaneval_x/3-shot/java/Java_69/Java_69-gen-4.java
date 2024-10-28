        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : lst) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        for (int num : freq.keySet()) {
            if (freq.get(num) >= num) {
                return num;
            }
        }
        return -1;
    }
}

