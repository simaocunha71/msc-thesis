        Map<Integer, Integer> freq_map = new HashMap<>();
        int max_freq = 0;
        int max_num = -1;

        for (int num : lst) {
            freq_map.put(num, freq_map.getOrDefault(num, 0) + 1);
            if (freq_map.get(num) >= num && num > max_num) {
                max_num = num;
                max_freq = freq_map.get(num);
            }
        }

        return max_freq == max_num ? max_num : -1;
    }
}