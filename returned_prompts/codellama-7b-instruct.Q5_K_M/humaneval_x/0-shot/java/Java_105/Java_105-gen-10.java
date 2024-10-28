        List<Integer> sortedList = arr.stream()
                .filter(num -> num >= 1 && num <= 9)
                .sorted()
                .collect(Collectors.toList());

        List<String> result = new ArrayList<>();
        for (int i = 0; i < sortedList.size(); i++) {
            int num = sortedList.get(i);
            String word = "One";
            switch (num) {
                case 1: word = "One"; break;
                case 2: word = "Two"; break;
                case 3: word = "Three"; break;
                case 4: word = "Four"; break;
                case 5: word = "Five"; break;
                case 6: word = "Six"; break;
                case 7: word = "Seven"; break;
                case 8: word = "Eight"; break;
                case 9: word = "Nine"; break;
            }
            result.add(word);
        }
        return result;
    }
}
