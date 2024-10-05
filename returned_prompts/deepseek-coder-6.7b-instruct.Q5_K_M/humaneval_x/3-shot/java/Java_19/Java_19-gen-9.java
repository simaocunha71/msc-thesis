        Map<String, Integer> numberMap = new HashMap<String, Integer>() {{
            put("zero", 0);
            put("one", 1);
            put("two", 2);
            put("three", 3);
            put("four", 4);
            put("five", 5);
            put("six", 6);
            put("seven", 7);
            put("eight", 8);
            put("nine", 9);
        }};

        List<String> numberList = Arrays.asList(numbers.split(" "));
        Collections.sort(numberList, new Comparator<String>() {
            public int compare(String s1, String s2) {
                return numberMap.get(s1) - numberMap.get(s2);
            }
        });

        return String.join(" ", numberList);
    }
}

