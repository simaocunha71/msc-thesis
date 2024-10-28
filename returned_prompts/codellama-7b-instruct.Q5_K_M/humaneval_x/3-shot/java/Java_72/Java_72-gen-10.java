        if (q.size() == 0) return false;
        if (q.size() == 1) return q.get(0) <= w;

        int sum = 0;
        for (int i = 0; i < q.size(); i++) {
            sum += q.get(i);
        }
        return sum <= w && isPalindromicList(q);
    }

    /**
    Determines if a list is a palindrome.
     */
    public boolean isPalindromicList(List<Integer> list) {
        if (list.size() == 0) {
            return false;
        }

        for (int i = 0; i < list.size() / 2; i++) {
            if (list.get(i) != list.get(list.size() - i - 1)) {
                return false;
            }
        }
        return true;
    }
}

