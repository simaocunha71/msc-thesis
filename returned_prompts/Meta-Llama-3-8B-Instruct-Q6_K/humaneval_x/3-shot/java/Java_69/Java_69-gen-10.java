        Map<Integer, Integer> frequencyMap = new HashMap<>();
        int max = 0;
        for (int num : lst) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
            if (num > max && frequencyMap.get(num) >= num) {
                max = num;
            }
        }
        return max > 0 ? max : -1;
    }
}

