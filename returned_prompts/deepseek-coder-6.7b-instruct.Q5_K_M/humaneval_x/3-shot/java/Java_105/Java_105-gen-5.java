        List<String> numNames = Arrays.asList("", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine");
        List<Integer> validNums = new ArrayList<>();

        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                validNums.add(num);
            }
        }

        Collections.sort(validNums, Collections.reverseOrder());

        List<String> result = new ArrayList<>();
        for (int num : validNums) {
            result.add(numNames.get(num));
        }

        return result;
    }
}

