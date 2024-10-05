        List<String> result = new ArrayList<>();
        List<Integer> sortedList = new ArrayList<>();
        for (int i : arr) {
            if (i >= 1 && i <= 9) {
                sortedList.add(i);
            }
        }
        Collections.sort(sortedList);
        for (int i = sortedList.size() - 1; i >= 0; i--) {
            switch (sortedList.get(i)) {
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