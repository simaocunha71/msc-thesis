        int minEven = Integer.MAX_VALUE;
        int index = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < minEven) {
                minEven = arr.get(i);
                index = i;
            }
        }
        if (index != -1) {
            return Arrays.asList(minEven, index);
        } else {
            return new ArrayList<>();
        }
    }
}