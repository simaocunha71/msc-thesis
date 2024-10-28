        int sum 		= sumList(q);
        boolean isBalanced = isPalindrome(q);
        return sum <= w && isBalanced;
    }

    private int sumList(List<Integer> list) {
        int sum 		= 0;
        for (int i : list) {
            sum += i;
        }
        return sum;
    }

    private boolean isPalindrome(List<Integer> list) {
        int start 		= 0;
        int end 		= list.size() - 1;

        while (start < end) {
            if (!list.get(start).equals(list.get(end))) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}

