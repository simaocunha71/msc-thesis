        Map<Integer, Integer> frequency = new HashMap<>();
        for (int num : lst) {
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }

        for (int num : lst) {
            if (num > 0 && frequency.get(num) >= num) {
                return num;
            }
        }
        return -1;
     }
}

