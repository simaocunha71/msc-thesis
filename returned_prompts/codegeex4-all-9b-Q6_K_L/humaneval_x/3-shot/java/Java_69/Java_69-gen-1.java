        Map<Integer, Integer> frequency = new HashMap<>();
        for (int i : lst) {
            frequency.put(i, frequency.getOrDefault(i, 0) + 1);
        }

        int result = -1;
        for (int i : lst) {
            if (frequency.get(i) >= i && i > result) result = i;
        }
        return result;
    }
}

