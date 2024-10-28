        Map<Integer, Integer> map = new HashMap<>();

        for (int n : lst) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        int max = -1;

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getKey() <= entry.getValue()) {
                max = Math.max(max, entry.getKey());
            }
        }

        return max;
    }
}

