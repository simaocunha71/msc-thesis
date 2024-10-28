        int max = -1;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i - 1) >= arr.get(i)) {
                max = i - 1;
                break;
            }
        }
        return max;
    }
}

