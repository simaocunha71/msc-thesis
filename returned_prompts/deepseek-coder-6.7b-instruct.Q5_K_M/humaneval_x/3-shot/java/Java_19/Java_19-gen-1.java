        Map<String, Integer> numeralMap = new HashMap<>();
        numeralMap.put("zero", 0);
        numeralMap.put("one", 1);
        numeralMap.put("two", 2);
        numeralMap.put("three", 3);
        numeralMap.put("four", 4);
        numeralMap.put("five", 5);
        numeralMap.put("six", 6);
        numeralMap.put("seven", 7);
        numeralMap.put("eight", 8);
        numeralMap.put("nine", 9);

        List<String> numeralList = Arrays.asList(numbers.split(" "));
        Collections.sort(numeralList, (a, b) -> numeralMap.get(a) - numeralMap.get(b));

        return String.join(" ", numeralList);
     }
}

