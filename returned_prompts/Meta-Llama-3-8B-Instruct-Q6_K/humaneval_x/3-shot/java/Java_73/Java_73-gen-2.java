        int changes = 0;
        int left = 0, right = arr.size() - 1;
        while (left < right) {
            if (arr.get(left) != arr.get(right)) {
                changes++;
                right--;
            } else {
                left++;
                right--;
            }
        }
        return changes;
    }
}