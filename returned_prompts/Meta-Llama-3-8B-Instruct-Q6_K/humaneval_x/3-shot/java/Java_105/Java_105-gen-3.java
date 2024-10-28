        List<String> result = new ArrayList<>();
        List<Integer> sorted_arr = new ArrayList<>();
        for (int num : arr) {
            if (1 <= num && num <= 9) {
                sorted_arr.add(num);
            }
        }
        Collections.sort(sorted_arr);
        for (int i = sorted_arr.size() - 1; i >= 0; i--) {
            result.add(getNumberName(sorted_arr.get(i)));
        }
        return result;
    }

    private String getNumberName(int num) {
        switch (num) {
            case 1: return "One";
            case 2: return "Two";
            case 3: return "Three";
            case 4: return "Four";
            case 5: return "Five";
            case 6: return "Six";
            case 7: return "Seven";
            case 8: return "Eight";
            case 9: return "Nine";
            default: return "";
        }
    }
}