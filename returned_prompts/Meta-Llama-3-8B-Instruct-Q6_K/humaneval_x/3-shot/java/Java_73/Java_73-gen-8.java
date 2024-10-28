        int n = arr.size();
        int left = 0, right = n - 1;
        int changes = 0;

        while (left < right) {
            if (arr.get(left) != arr.get(right)) {
                changes++;
            }
            left++;
            right--;
        }
        return changes;
    }
}

