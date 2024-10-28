        Map<Integer, Integer> freq_map = new HashMap<>();
        for (int num : lst) freq_map.put(num, freq_map.getOrDefault(num, 0) + 1);
        Collections.sort(lst, Collections.reverseOrder());
        for  (int num : lst) {
            if  (freq_map.get(num) >= num) return num;
        }
        return -1;
    }
}

