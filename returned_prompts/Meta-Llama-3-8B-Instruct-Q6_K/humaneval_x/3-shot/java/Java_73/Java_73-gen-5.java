        int left = 0;
        int right = arr.size() - 1;
        int change = 0;

        while (left < right) {
            if (arr.get(left) != arr.get(right)) {
                change++;
                left++;
            } else {
                left++;
                right--;
            }
        }
        return change;
    }
}

