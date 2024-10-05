        int smallestEvenValue = Integer.MAX_VALUE;
        int smallestEvenIndex = -1;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < smallestEvenValue && arr.get(i) % 2 == 0) {
                smallestEvenValue = arr.get(i);
                smallestEvenIndex = i;
            }
        }

        if (smallestEvenIndex == -1) {
            return new ArrayList<>();
        } else {
            return Arrays.asList(smallestEvenValue, smallestEvenIndex);
        }
    }
}

