        Map<Integer, Integer> counts = new HashMap<>();
        for (Integer num : numbers) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        return numbers.stream()
                .filter(num -> counts.get(num) == 1)
                .collect(Collectors.toList());
     }
}

