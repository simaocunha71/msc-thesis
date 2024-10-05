        int sum = q.stream().reduce(0, Integer::sum);
        return w >= sum && isPalindrome(q);
    }

    private boolean isPalindrome(List<Integer> q) {
        return q.equals(new ArrayList<>(q.stream().map(i -> i).sorted(Collections.reverseOrder()).collect(Collectors.toList())));
    }
}

