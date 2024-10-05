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
            String num_name = "";
            switch (num) {
                case 1:
                    num_name = "One";
                    break;
                case 2:
                    num_name = "Two";
                    break;
                case 3:
                    num_name = "Three";
                    break;
                case 4:
                    num_name = "Four";
                    break;
                case 5:
                    num_name = "Five";
                    break;
                case 6:
                    num_name = "Six";
                    break;
                case 7:
                    num_name = "Seven";
                    break;
                case 8:
                    num_name = "Eight";
                    break;
                case 9:
                    num_name = "Nine";
                    break;
            }
            result.add(num_name);
        }
        return result;
    }
}

