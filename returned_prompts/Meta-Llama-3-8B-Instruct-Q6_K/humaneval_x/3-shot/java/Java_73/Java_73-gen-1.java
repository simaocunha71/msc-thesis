        int changes = 0;
        int left = 0, right = arr.size() - 1;
        while (left < right) {
            if (arr.get(left) != arr.get(right)) {
                changes++;
                if (arr.get(left) > arr.get(right)) {
                    arr.set(left, arr.get(right));
                } else {
                    arr.set(right, arr.get(left));
                }
            }
            left++;
            right--;
        }
        return changes;
    }
}

