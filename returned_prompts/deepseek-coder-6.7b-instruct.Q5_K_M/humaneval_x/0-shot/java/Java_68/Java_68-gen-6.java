        int min = Integer.MAX_VALUE;
        int minIndex = -1;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < min && arr.get(i) % 2 == 0) {
                min = arr.get(i);
                minIndex = i;
            }
        }

        if (minIndex == -1) {
            return new ArrayList<>();
        } else {
            return Arrays.asList(min, minIndex);
        }
    }
}

This code works by iterating over the input array and checking each node to see if it is an even number and if it is smaller than the current smallest even number. If it is smaller, then it updates the smallest even number and its index. Finally, it returns a list containing the smallest even number and its index. If there are no even numbers, it returns an empty list.

The time complexity of this code is O(n), where n is the size of the input array, because it iterates over the array once. The space complexity is O(1), because it only uses a constant amount of space to store the smallest even number and its index.
