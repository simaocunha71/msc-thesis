        int maxIndex = -1;
        for (int i = 0; i < arr.size() - 1; i++) {
            if (arr.get(i) < arr.get(i + 1)) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }
}
