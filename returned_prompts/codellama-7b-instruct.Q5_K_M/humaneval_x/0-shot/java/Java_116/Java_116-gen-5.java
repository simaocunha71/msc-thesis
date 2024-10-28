        List<Integer> ret = arr;
        for (int i = 0; i < arr.size(); i++) {
            for (int j = i + 1; j < arr.size(); j++) {
                if (countOnes(arr.get(i)) < countOnes(arr.get(j))) {
                    Collections.swap(ret, i, j);
                } else if (countOnes(arr.get(i)) == countOnes(arr.get(j)) && arr.get(i) > arr.get(j)) {
                    Collections.swap(ret, i, j);
                }
            }
        }
        return ret;
    }

    private int countOnes(int i) {
        int count = 0;
        while (i != 0) {
            if (i % 2 == 1) {
                count++;
            }
            i >>= 1;
        }
        return count;
    }
}






