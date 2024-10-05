        List<String> result = new ArrayList<>();
        Map<Integer, String> map = new HashMap<>();
        map.put(1, "One");
        map.put(2, "Two");
        map.put(3, "Three");
        map.put(4, "Four");
        map.put(5, "Five");
        map.put(6, "Six");
        map.put(7, "Seven");
        map.put(8, "Eight");
        map.put(9, "Nine");

        arr.stream()
                .filter(n -> n > 0 && n < 10)
                .sorted()
                .forEach(n -> result.add(map.get(n)));

        return result;
    }
}

