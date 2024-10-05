        int minEvenVal = Integer.MAX_VALUE;
        int minEvenIndex = -1;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < minEvenVal && arr.get(i) % 2 == 0) {
                minEvenVal = arr.get(i);
                minEvenIndex = i;
            }
        }

        if (minEvenIndex == -1) {
            return new ArrayList<>();
        } else {
            return Arrays.asList(minEvenVal, minEvenIndex);
        }
     }
}

