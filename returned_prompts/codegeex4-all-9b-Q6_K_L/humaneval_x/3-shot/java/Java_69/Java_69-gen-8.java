        Map<Integer, Integer> counts = new HashMap<>();
        for (int i : lst) {
            counts.put(i, counts.getOrDefault(i, 0) + 1);
        }
        int max = -1;
        for (int i : counts.keySet()) {
            if (i <= counts.get(i)) {
                max = Math.max(max, i);
            }
        }
        return max;
    }
}

