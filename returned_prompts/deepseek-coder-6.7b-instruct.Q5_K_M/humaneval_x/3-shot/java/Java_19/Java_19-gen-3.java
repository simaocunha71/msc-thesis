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
        numberList.sort(Comparator.comparing(numberMap::get));

        return String.join(" ", numberList);
     }
}

