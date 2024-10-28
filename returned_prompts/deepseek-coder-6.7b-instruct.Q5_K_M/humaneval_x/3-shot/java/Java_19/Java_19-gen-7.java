        Map<String, Integer> numberMap = new HashMap<>();
        numberMap.put("zero", 0);
        numberMap.put("one", 1);
        numberMap.put("two", 2);
        numberMap.put("three", 3);
        numberMap.put("four", 4);
        numberMap.put("five", 5);
        numberMap.put("six", 6);
        numberMap.put("seven", 7);
        numberMap.put("eight", 8);
        numberMap.put("nine", 9);

        List<String> numberList = Arrays.asList(numbers.split(" "));
        Collections.sort(numberList, new Comparator<String>() {
            public int compare(String s1, String s2) {
                return numberMap.get(s1) - numberMap.get(s2);
            }
        });

        return String.join(" ", numberList);
    }
}

