        int left = 0;
        int right = arr.size() - 1;
        int changes = 0;

        while (left < right) {
            if (arr.get(left) != arr.get(right)) {
                changes += 1;
            }
            left += 1;
            right -= 1;
        }
        return changes;
    }
}

