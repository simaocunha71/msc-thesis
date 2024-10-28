        List<String> result = new ArrayList<>();
        List<Integer> sorted_array = new ArrayList<>();
        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                sorted_array.add(num);
            }
        }
        Collections.sort(sorted_array);
        for (int i = sorted_array.size() - 1; i >= 0; i--) {
            String digit_name = "";
            switch (sorted_array.get(i)) {
                case 1:
                    digit_name = "One";
                    break;
                case 2:
                    digit_name = "Two";
                    break;
                case 3:
                    digit_name = "Three";
                    break;
                case 4:
                    digit_name = "Four";
                    break;
                case 5:
                    digit_name = "Five";
                    break;
                case 6:
                    digit_name = "Six";
                    break;
                case 7:
                    digit_name = "Seven";
                    break;
                case 8:
                    digit_name = "Eight";
                    break;
                case 9:
                    digit_name = "Nine";
                    break;
            }
            result.add(digit_name);
        }
        return result;
    }
}

