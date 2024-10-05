        Collections.sort(lst, Collections.reverseOrder());
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : lst) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
            if (num >= freq.get(num)) {
                return num;
            }
        }
        return -1;
    }
}

