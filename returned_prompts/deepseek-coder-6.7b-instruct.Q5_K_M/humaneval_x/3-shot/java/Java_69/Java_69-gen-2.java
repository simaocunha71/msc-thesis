        Map<Integer, Integer> freq = new HashMap<>();
        for (int i : lst) {
            freq.put(i, freq.getOrDefault(i, 0) + 1);
        }
        Collections.sort(lst);
        for (int i : lst) {
            if (i > 0 && freq.get(i) >= i) {
                return i;
            }
        }
        return -1;
     }
}

