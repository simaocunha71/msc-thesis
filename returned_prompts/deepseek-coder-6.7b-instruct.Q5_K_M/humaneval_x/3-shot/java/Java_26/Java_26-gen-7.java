        Map<Integer, Integer> counts = new HashMap<>();
        for (int number : numbers) {
            counts.put(number, counts.getOrDefault(number, 0) + 1);
        }

        return numbers.stream()
                .filter(number -> counts.get(number) == 1)
                .collect(Collectors.toList());
    }
}

