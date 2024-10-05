        List<String> result = new ArrayList<>();

        if (arr.size() == 0) {
            return result;
        }

        // sort the array
        arr.sort(Comparator.naturalOrder());

        // reverse the array
        Collections.reverse(arr);

        // ignore the strange numbers
        List<Integer> new_arr = new ArrayList<>();
        for (Integer num : arr) {
            if (num <= 9 && num >= 1) {
                new_arr.add(num);
            }
        }

        // convert the sorted array to string array
        List<String> name_arr = new ArrayList<>();
        for (Integer num : new_arr) {
            switch (num) {
                case 1:
                    result.add("One");
                    break;
                case 2:
                    result.add("Two");
                    break;
                case 3:
                    result.add("Three");
                    break;
                case 4:
                    result.add("Four");
                    break;
                case 5:
                    result.add("Five");
                    break;
                case 6:
                    result.add("Six");
                    break;
                case 7:
                    result.add("Seven");
                    break;
                case 8:
                    result.add("Eight");
                    break;
                case 9:
                    result.add("Nine");
                    break;
            }
        }
        return result;
    }
}

