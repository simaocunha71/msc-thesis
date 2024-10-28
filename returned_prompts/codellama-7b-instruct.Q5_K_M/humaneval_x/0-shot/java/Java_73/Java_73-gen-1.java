        int min = Integer.MAX_VALUE;
        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < arr.size(); j++) {
                if (i == j) continue;
                if (arr.get(i) > arr.get(j)) {
                    min = Math.min(min, arr.get(i) - arr.get(j));
                    continue A;
                }
            }
        }
        return min;
    }
}

