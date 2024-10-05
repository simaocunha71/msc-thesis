        // 1. find the smallest even number in the array
        // 2. find the index of that number
        // 3. return [smallest_even_value, index_of_smallest_even_value]
        List<Integer> result = new ArrayList<>();
        int smallestEvenValue = 0;
        int smallestIndex = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0) {
                if (smallestEvenValue == 0) {
                    smallestEvenValue = arr.get(i);
                    smallestIndex = i;
                } else if (arr.get(i) < smallestEvenValue) {
                    smallestEvenValue = arr.get(i);
                    smallestIndex = i;
                }
            }
        }
        result.add(smallestEvenValue);
        result.add(smallestIndex);
        return result;
    }
}
