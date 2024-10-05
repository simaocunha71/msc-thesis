        if (!isPalindrome(q)) {
            return false;
        }
        int sum = 0;
        for (int num : q) {
            sum += num;
        }
        return sum <= w;
    }

    private boolean isPalindrome(List<Integer> list) {
        List<Integer> reversed = new ArrayList<>(list);
        Collections.reverse(reversed);
        return list.equals(reversed);
    }
}

