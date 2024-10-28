        int left = 0, right = arr.size() - 1;
        int result = 0;

        while (left < right) {
            if (arr.get(left) != arr.get(right)) {
                result += 1;
            }
            left += 1;
            right -= 1;
        }
        return result;
    }
}

