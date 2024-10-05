        int maxIndex = -1;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) <= arr.get(i - 1)) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }
}