        int sum = 0;
        for (int i : q) {
            sum += i;
        }
        if (sum > w) {
            return false;
        }
        if (!isPalindrome(q)) {
            return false;
        }
        return true;
    }

    private boolean isPalindrome(List<Integer> list) {
        int left = 0, right = list.size() - 1;
        while (left < right) {
            if (!list.get(left).equals(list.get(right))) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}

