        int max_frequency = 0;
        int result = -1;
        Map<Integer, Integer> frequency = new HashMap<>();

        for (int i = 0; i < lst.size(); i++) {
            int num = lst.get(i);
            if (frequency.containsKey(num)) {
                frequency.put(num, frequency.get(num) + 1);
            } else {
                frequency.put(num, 1);
            }

            if (frequency.get(num) > max_frequency) {
                result = num;
                max_frequency = frequency.get(num);
            }
        }

        for (Map.Entry<Integer, Integer> entry : frequency.entrySet()) {
            if (entry.getValue() >= entry.getKey() && entry.getKey() > result) {
                result = entry.getKey();
            }
        }
        return result;
    }
}

