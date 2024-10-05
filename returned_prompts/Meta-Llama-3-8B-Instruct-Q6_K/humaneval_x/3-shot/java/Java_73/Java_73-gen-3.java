        int changes = 0;
        int left = 0, right = arr.size() - 1;
        while (left < right) {
            if (arr.get(left) != arr.get(right)) {
                changes++;
                int min = Math.min(arr.get(left), arr.get(right));
                arr.set(left, min);
                arr.set(right, min);
                right--;
            } else {
                left++;
                right--;
            }
        }
        return changes;
    }
}

