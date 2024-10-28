        if (arr.size() <= 1) {
            return true;
        }

        int lastElement = arr.get(arr.size() - 1);
        int lastElementIndex = arr.size() - 1;
        int lastNonDecreasingIndex = -1;

        for (int i = arr.size() - 2; i >= 0; i--) {
            if (arr.get(i) < lastElement) {
                lastNonDecreasingIndex = i;
                break;
            }
        }

        // check if last non-decreasing index is present
        if (lastNonDecreasingIndex != -1) {
            if (lastElementIndex != lastNonDecreasingIndex) {
                // swap last element with last non-decreasing element
                arr.set(lastNonDecreasingIndex, lastElement);
                arr.set(lastElementIndex, arr.get(lastNonDecreasingIndex));
                return true;
            }
        }

        return false;
    }

    public boolean moveAllBalls(List<Integer> arr) {
        if (arr.size() <= 1) {
            return true;
        }

        int lastElement = arr.get(arr.size() - 1);
        int lastElementIndex = arr.size() - 1;

        int lastNonDecreasingIndex = -1;

        for (int i = arr.size() - 2; i >= 0; i--) {
            if (arr.get(i) < lastElement) {
                lastNonDecreasingIndex = i;
                break;
            }
        }

        // check if last non-decreasing index is present
        if (lastNonDecreasingIndex != -1) {
            if (lastElementIndex != lastNonDecreasingIndex) {
                // swap last element with last non-decreasing element
                arr.set(lastNonDecreasingIndex, lastElement);
                arr.set(lastElementIndex, arr.get(lastNonDecreasingIndex));
            }
        }

        // check if array is sorted
        int prev = -1;