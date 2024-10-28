        List<String> result = new ArrayList<>();
        List<Integer> filtered_arr = new ArrayList<>();

        for (int n : arr) {
            if (n > 0 && n < 10) filtered_arr.add(n);
        }

        Collections.sort(filtered_arr);
        Collections.reverse(filtered_arr);

        for (int n : filtered_arr) {
            result.add(numberToString(n));
        }

        return result;
    }

    private String numberToString(int number) {
        switch (number) {
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

