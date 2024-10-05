        Map<String, Integer> numeralMapping = new HashMap<>();
        numeralMapping.put("zero", 0);
        numeralMapping.put("one", 1);
        numeralMapping.put("two", 2);
        numeralMapping.put("three", 3);
        numeralMapping.put("four", 4);
        numeralMapping.put("five", 5);
        numeralMapping.put("six", 6);
        numeralMapping.put("seven", 7);
        numeralMapping.put("eight", 8);
        numeralMapping.put("nine", 9);

        List<String> numeralList = Arrays.asList(numbers.split(" "));
        numeralList.sort(Comparator.comparing(numeral -> numeralMapping.get(numeral)));

        return String.join(" ", numeralList);
     }
}

