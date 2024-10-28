        int max = -1;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i - 1) >= arr.get(i)) {
                return i - 1;
            }
            max = Math.max(max, i);
        }
        return max;
    }
}

