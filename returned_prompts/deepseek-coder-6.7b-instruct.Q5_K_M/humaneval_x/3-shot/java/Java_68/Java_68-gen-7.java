        int smallestEvenValue = Integer.MAX_VALUE;
        int smallestEvenIndex = -1;

        for (int i = 0; i < arr.size(); i++) {
            int currentValue = arr.get(i);
            if (currentValue < smallestEvenValue && currentValue % 2 == 0) {
                smallestEvenValue = currentValue;
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

