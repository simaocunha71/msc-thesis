        List<Integer> temp = new ArrayList<Integer>();
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > 0 && arr.get(i) < 10) {
                temp.add(arr.get(i));
            }
        }
        temp.sort(Comparator.naturalOrder());
        Collections.reverse(temp);
        List<String> result = new ArrayList<>();
        for (int i = 0; i < temp.size(); i++) {
            if (temp.get(i) == 1) {
                result.add("One");
            } else if (temp.get(i) == 2) {
                result.add("Two");
            } else if (temp.get(i) == 3) {
                result.add("Three");
            } else if (temp.get(i) == 4) {
                result.add("Four");
            } else if (temp.get(i) == 5) {
                result.add("Five");
            } else if (temp.get(i) == 6) {
                result.add("Six");
            } else if (temp.get(i) == 7) {
                result.add("Seven");
            } else if (temp.get(i) == 8) {
                result.add("Eight");
            } else if (temp.get(i) == 9) {
                result.add("Nine");
            }
        }
        return result;
    }
}

