        List<String> result = new ArrayList<>();
        List<Integer> sorted_arr = new ArrayList<>();
        List<Integer> reverse_arr = new ArrayList<>();

        for (int i : arr) {
            if (i > 0 && i < 10) {
                sorted_arr.add(i);
            }
        }

        sorted_arr.sort(null);
        reverse_arr.addAll(sorted_arr);
        reverse_arr.sort(Collections.reverseOrder());

        for (int i : reverse_arr) {
            if (i > 0 && i < 10) {
                result.add(nameByIndex(i));
            }
        }
        return result;
    }

    public String nameByIndex(int i) {
        switch (i) {
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
        }
        return "";
    }
}

