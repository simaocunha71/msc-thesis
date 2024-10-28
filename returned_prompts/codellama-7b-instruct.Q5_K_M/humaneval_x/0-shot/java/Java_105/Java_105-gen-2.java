        List<String> result = new ArrayList<>();
        if (arr.size() == 0) {
            return result;
        }
        List<String> numToWord = new ArrayList<>();
        numToWord.add("One");
        numToWord.add("Two");
        numToWord.add("Three");
        numToWord.add("Four");
        numToWord.add("Five");
        numToWord.add("Six");
        numToWord.add("Seven");
        numToWord.add("Eight");
        numToWord.add("Nine");

        List<Integer> sorted = arr.stream().filter(x -> x >= 1 && x <= 9).sorted().collect(Collectors.toList());
        List<Integer> reversed = sorted.stream().sorted((x, y) -> y - x).collect(Collectors.toList());
        for (Integer num : reversed) {
            result.add(numToWord.get(num - 1));
        }
        return result;
    }
}

