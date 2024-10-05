public boolean moveOneBall(List<Integer> arr) {
        if (arr.size() == 0) {
            return true;
        }
        List<Integer> sortedArr = new ArrayList<>(arr);
        Collections.sort(sortedArr);

        int minIndex = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) == sortedArr.get(0)) {
                minIndex = i;
                break;
            }
        }

        int count = 0;
        while (count < arr.size()) {
            if (arr.get((minIndex + count) % arr.size()) != sortedArr.get(count)) {
                return false;
            }
            count++;
        }

        return true;
    }
