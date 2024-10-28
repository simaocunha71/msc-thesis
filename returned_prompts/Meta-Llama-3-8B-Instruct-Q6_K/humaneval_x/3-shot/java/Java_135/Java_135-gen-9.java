        int maxIndex = -1;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i - 1) >= arr.get(i)) {
                maxIndex = i - 1;
                break;
            }
        }
        return maxIndex;
    }
}

