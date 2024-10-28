        return q.stream().mapToInt(i -> i).sum() <= w && isPalindrome(q);
    }

    private boolean isPalindrome(List<Integer> list) {
        for (int i = 0; i < list.size() / 2; i++) {
            if (list.get(i) != list.get(list.size() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}

