        Map<String, Integer> mapping = new HashMap<>();
        mapping.put("zero", 0);
        mapping.put("one", 1);
        mapping.put("two", 2);
        mapping.put("three", 3);
        mapping.put("four", 4);
        mapping.put("five", 5);
        mapping.put("six", 6);
        mapping.put("seven", 7);
        mapping.put("eight", 8);
        mapping.put("nine", 9);
        String[] numbers_array = numbers.split(" ");
        Arrays.sort(numbers_array, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return mapping.get(o1) - mapping.get(o2);
            }
        });
        return String.join(" ", numbers_array);
    }
}

