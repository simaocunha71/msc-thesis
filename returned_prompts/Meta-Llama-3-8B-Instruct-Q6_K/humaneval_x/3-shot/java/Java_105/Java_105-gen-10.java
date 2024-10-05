        List<String> result = new ArrayList<>();
        List<Integer> sortedList = new ArrayList<>();
        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                sortedList.add(num);
            }
        }
        Collections.sort(sortedList);
        Collections.reverse(sortedList);
        for (int num : sortedList) {
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

