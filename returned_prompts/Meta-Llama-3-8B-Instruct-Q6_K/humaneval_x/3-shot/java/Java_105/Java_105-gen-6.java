        List<String> result = new ArrayList<>();
        List<Integer> sorted_numbers = new ArrayList<>();

        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                sorted_numbers.add(num);
            }
        }

        Collections.sort(sorted_numbers);

        for (int i = sorted_numbers.size() - 1; i >= 0; i--) {
            int num = sorted_numbers.get(i);
            result.add(getName(num));
        }

        return result;
    }

    private String getName(int num) {
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