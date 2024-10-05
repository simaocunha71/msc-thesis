        int sum = q.stream().mapToInt(x -> x).sum();
        return sum <= w && isPalindrome(q);
    }

    private boolean isPalindrome(List<Integer> q) {
        int left = 0;
        int right = q.size() - 1;
        while (left < right) {
            if (q.get(left) != q.get(right)) return false;
            left += 1;
            right -= 1;
        }
        return true;
    }
}

