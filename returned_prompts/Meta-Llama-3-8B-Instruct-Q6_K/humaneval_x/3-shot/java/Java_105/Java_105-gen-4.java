        List<String> result = new ArrayList<>();
        List<Integer> numbers = new ArrayList<>();
        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                numbers.add(num);
            }
        }
        if (numbers.isEmpty()) {
            return result;
        }
        Collections.sort(numbers);
        Collections.reverse(numbers);
        for (int num : numbers) {
            result.add(getDigitName(num));
        }
        return result;
    }

    private String getDigitName(int num) {
        switch (num) {
            case 1:
                return "One";
            case 2:
                return "Two";
            case 3:
                return "Three";
            case 4:
                return "Four";
            case 5:
                return "Five";
            case 6:
                return "Six";
            case 7:
                return "Seven";
            case 8:
                return "Eight";
            case 9:
                return "Nine";
            default:
                return "";
        }
    }
}