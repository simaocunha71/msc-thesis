        Map<Integer, Integer> frequency = new HashMap<>();
        for (int num : lst) {
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }
        for (int num : new TreeSet<>(frequency.keySet())) {
            if (num >= frequency.get(num)) {
                return num;
            }
        }
        return -1;
    }
}

