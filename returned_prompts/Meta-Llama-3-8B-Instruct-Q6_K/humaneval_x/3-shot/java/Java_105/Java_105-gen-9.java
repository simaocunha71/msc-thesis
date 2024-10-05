        List<String> result = new ArrayList<>();
        List<Integer> sorted_arr = new ArrayList<>();

        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                sorted_arr.add(num);
            }
        }

        Collections.sort(sorted_arr);
        Collections.reverse(sorted_arr);

        for (int num : sorted_arr) {
            result.add(getNumberName(num));
        }

        return result;
    }

    private String getNumberName(int num) {
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

