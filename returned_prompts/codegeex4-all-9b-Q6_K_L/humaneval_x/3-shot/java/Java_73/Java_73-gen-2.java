        int left = 0;
        int right = arr.size() - 1;
        int count = 0;

        while (left < right) {
            if (arr.get(left) != arr.get(right)) {
                count++;
            }
            left++;
            right--;
        }

        return count;
    }
}

