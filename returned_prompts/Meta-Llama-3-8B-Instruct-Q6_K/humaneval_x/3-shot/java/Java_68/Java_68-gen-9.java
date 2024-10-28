        int minIndex = -1;
        int minEvenValue = Integer.MAX_VALUE;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < minEvenValue) {
                minEvenValue = arr.get(i);
                minIndex = i;
            }
        }
        if (minIndex != -1) {
            return Arrays.asList(minEvenValue, minIndex);
        } else {
            return new ArrayList<>();
        }
    }
}

