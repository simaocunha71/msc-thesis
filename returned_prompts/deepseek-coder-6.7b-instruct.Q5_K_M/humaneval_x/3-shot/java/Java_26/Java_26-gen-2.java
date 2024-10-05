        Map<Integer, Integer> counts = new HashMap<>();
        List<Integer> result = new ArrayList<>();

        for (int num : numbers) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }

        for (int num : numbers) {
            if (counts.get(num) == 1) {
                result.add(num);
            } else {
                counts.put(num, 0);
            }
        }

        return result;
    }
}

