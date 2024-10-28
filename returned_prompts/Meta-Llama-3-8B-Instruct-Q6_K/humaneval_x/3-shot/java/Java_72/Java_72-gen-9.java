        int sum = 0;
        for (int i = 0; i < q.size(); i++) {
            sum += q.get(i);
        }
        if (sum > w) {
            return false;
        }
        List<Integer> q_copy = new ArrayList<>(q);
        Collections.reverse(q_copy);
        for (int i = 0; i < q_copy.size(); i++) {
            if (!q.get(i).equals(q_copy.get(i))) {
                return false;
            }
        }
        return true;
    }
}

