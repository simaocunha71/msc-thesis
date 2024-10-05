        return (q.stream().reduce((a, b) -> a + b).get() <= w) && isPalindrome(q);
    }

    public boolean isPalindrome(List<Integer> q) {
        int left = 0, right = q.size() - 1;
        while (left < right) {
            if (q.get(left) != q.get(right)) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;
    }
}



```