        int min = Integer.MAX_VALUE;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < min) {
                min = arr.get(i);
            }
        }
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) != min) {
                if (arr.get(i - 1) < arr.get(i)) {
                    return false;
                }
            }
        }
        return true;
    }
}

